package com.flrndttrch.smartcouch.rest;

import android.text.TextUtils;

import com.flrndttrch.smartcouch.model.Lighting;
import com.flrndttrch.smartcouch.model.Type;
import com.flrndttrch.smartcouch.model.TypeResponse;
import com.flrndttrch.smartcouch.model.User;
import com.flrndttrch.smartcouch.model.UserResponse;

import java.util.HashMap;
import java.util.List;

import okhttp3.Credentials;
import okhttp3.OkHttpClient;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;
import retrofit2.http.Body;
import retrofit2.http.GET;
import retrofit2.http.POST;
import retrofit2.http.Path;
import retrofit2.http.Query;

public interface DjangoService {
    @GET("types/")
    Call<TypeResponse> listTypes();

    @GET("types/")
    Call<TypeResponse> getTypeByName(@Query("name") String name);

    @GET("users/")
    Call<UserResponse> listUsers();

    @GET("users/")
    Call<UserResponse> getUserByName(@Query("name") String name);

    @POST("lightings/")
    Call<Lighting> postLighting(@Body Lighting lighting);

}
