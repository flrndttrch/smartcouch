package com.flrndttrch.smartcouch;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {
    private Button mLightingButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mLightingButton = findViewById(R.id.lightingButton);
        mLightingButton.setOnClickListener(this);
    }

    @Override
    public void onClick(View v) {
        Intent intent = getIntent();
        Bundle extras = intent.getExtras();
        Intent toLed = new Intent(this, LedActivity.class);
        toLed.putExtras(extras);
        startActivity(toLed);
        finish();
    }
}
