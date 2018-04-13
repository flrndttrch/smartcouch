package com.flrndttrch.smartcouch;

import android.content.DialogInterface;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.SeekBar;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Toast;

import com.flrndttrch.smartcouch.model.Lighting;
import com.flrndttrch.smartcouch.model.LightingResponse;
import com.flrndttrch.smartcouch.model.Type;
import com.flrndttrch.smartcouch.model.TypeResponse;
import com.flrndttrch.smartcouch.model.User;
import com.flrndttrch.smartcouch.model.UserResponse;
import com.flrndttrch.smartcouch.rest.DjangoService;
import com.flrndttrch.smartcouch.rest.ServiceGenerator;
import com.skydoves.colorpickerpreference.ColorEnvelope;
import com.skydoves.colorpickerpreference.ColorListener;
import com.skydoves.colorpickerpreference.ColorPickerDialog;
import com.skydoves.colorpickerpreference.ColorPickerView;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class LedActivity extends AppCompatActivity implements AdapterView.OnItemSelectedListener, SeekBar
        .OnSeekBarChangeListener, View.OnClickListener {
    private static final String TAG = LedActivity.class.getSimpleName();
    private TextView colorTextView;
    private ImageView colorView;
    private android.app.AlertDialog alertDialog;
    private Spinner typeSpinner;
    private SeekBar brightnessSeekbar;
    private Button submit;
    private List<Type> types;
    private SharedPreferences settings;
    private int[] color = {255, 255, 255};
    private float brightness;
    private DjangoService djangoService;
    private User user;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_led);
        colorTextView = findViewById(R.id.colorTextView);
        colorView = findViewById(R.id.color);
        colorView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                showDialog();
            }
        });
        typeSpinner = findViewById(R.id.typeSpinner);
        typeSpinner.setOnItemSelectedListener(this);
        List<String> typesStrings = new ArrayList<String>();
        if (types != null) {
            typesStrings = types.stream().map(type -> type.getName()).collect(Collectors.toList());
        }
        ArrayAdapter<String> spinnerAdapter = new ArrayAdapter<String>(LedActivity.this, android.R.layout
                .simple_spinner_item, typesStrings);
        spinnerAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        typeSpinner.setAdapter(spinnerAdapter);
        brightnessSeekbar = findViewById(R.id.brightnessSeekbar);
        brightnessSeekbar.setOnSeekBarChangeListener(this);
        submit = findViewById(R.id.submit);
        submit.setOnClickListener(this);

        settings = getSharedPreferences("UserInfo", 0);
        djangoService =
                ServiceGenerator.createService(DjangoService.class, settings.getString("Username", "").toString(),
                        settings.getString("Password", "").toString());
        djangoService.listTypes().enqueue(new Callback<TypeResponse>() {
            @Override
            public void onResponse(Call<TypeResponse> call, Response<TypeResponse> response) {
//                List<Movie> movies = response.body().getResults();
                types = response.body().getResults();
                List<String> typesStrings = types.stream().map(type -> type.getName()).collect(Collectors.toList());
                ArrayAdapter<String> spinnerAdapter = new ArrayAdapter<String>(LedActivity.this, android.R.layout
                        .simple_spinner_item, typesStrings);
                spinnerAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
                typeSpinner.setAdapter(spinnerAdapter);
                Log.d(TAG, "Number of types received: " + types.size());
            }

            @Override
            public void onFailure(Call<TypeResponse> call, Throwable throwable) {
                Toast.makeText(LedActivity.this, R.string.error_types, Toast.LENGTH_SHORT).show();
                Log.e(TAG, throwable.toString());
            }
        });
        djangoService.getUserByName(settings.getString("username", "")).enqueue(new Callback<UserResponse>() {
            @Override
            public void onResponse(Call<UserResponse> call, Response<UserResponse> response) {
                List<User> results = response.body().getResults();
                if (!results.isEmpty()) {
                    user = results.get(0);
                }
            }

            @Override
            public void onFailure(Call<UserResponse> call, Throwable t) {

            }
        });


        ColorPickerDialog.Builder builder = new ColorPickerDialog.Builder(this, R.style.AppTheme);
        builder.setTitle("ColorPicker Dialog");
        builder.setPreferenceName("MyColorPickerDialog");
        //builder.setFlagView(new CustomFlag(this, R.layout.layout_flag));
        builder.setPositiveButton(getString(R.string.confirm), new ColorListener() {
            @Override
            public void onColorSelected(ColorEnvelope colorEnvelope) {
                colorTextView.setText("#" + colorEnvelope.getColorHtml());
                color = colorEnvelope.getColorRGB();
                colorView.setBackgroundColor(colorEnvelope.getColor());
            }
        });
        builder.setNegativeButton(getString(R.string.cancel), new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialogInterface, int i) {
                dialogInterface.dismiss();
            }
        });

        alertDialog = builder.create();

        /**
         * get ColorPicker from builder, and set views as saved data
         */
        ColorPickerView colorPickerView = builder.getColorPickerView();

        colorTextView = findViewById(R.id.colorTextView);
        colorTextView.setText("#" + colorPickerView.getSavedColorHtml(R.color.colorAccent));
        color = colorPickerView.getSavedColorRGB(R.color.colorAccent);

        colorView.setBackgroundColor(colorPickerView.getSavedColor(R.color.colorAccent));
    }

    @Override
    public void onItemSelected(AdapterView<?> adapterView, View view, int i, long l) {
        String type = adapterView.getItemAtPosition(i).toString().toLowerCase();
        if (type.equals("off") || type.equals("rainbow")) {
            colorView.setVisibility(View.GONE);
            colorTextView.setVisibility(View.GONE);
            if (type.equals("off")) {
                brightnessSeekbar.setVisibility(View.GONE);
            } else if (type.equals("rainbow")) {
                brightnessSeekbar.setVisibility(View.VISIBLE);
            }
        } else if (type.equals("color") || type.equals("blink")) {
            colorView.setVisibility(View.VISIBLE);
            colorTextView.setVisibility(View.VISIBLE);
            brightnessSeekbar.setVisibility(View.VISIBLE);
        }
    }

    @Override
    public void onNothingSelected(AdapterView<?> adapterView) {

    }

    @Override
    public void onProgressChanged(SeekBar seekBar, int i, boolean b) {
        brightness = (float) i / 100;
    }

    @Override
    public void onStartTrackingTouch(SeekBar seekBar) {

    }

    @Override
    public void onStopTrackingTouch(SeekBar seekBar) {

    }

    @Override
    public void onClick(View view) {
        String typeName = typeSpinner.getSelectedItem().toString();
        if (typeName == null) {
            Toast.makeText(this, R.string.error_type, Toast.LENGTH_SHORT);
            return;
        }
        djangoService.getTypeByName(typeName).enqueue(new Callback<TypeResponse>() {
            @Override
            public void onResponse(Call<TypeResponse> call, Response<TypeResponse> response) {
                List<Type> results = response.body().getResults();
                if (!results.isEmpty()) {
                    Type type = results.get(0);
                    submitLighting(type);
                }
            }

            @Override
            public void onFailure(Call<TypeResponse> call, Throwable t) {

            }
        });

    }

    public void submitLighting(Type type) {
        Lighting lighting = new Lighting(brightness, color[0], color[1], color[2], null, null,type, user);
        djangoService.postLighting(lighting).enqueue(new Callback<Lighting>() {
            @Override
            public void onResponse(Call<Lighting> call, Response<Lighting> response) {
                Log.d(TAG, "Created new Lighting");
                Toast.makeText(LedActivity.this, R.string.success_lighting, Toast.LENGTH_SHORT);
            }

            @Override
            public void onFailure(Call<Lighting> call, Throwable t) {

            }
        });
    }

    public void showDialog() {
        alertDialog.show();
    }
}
