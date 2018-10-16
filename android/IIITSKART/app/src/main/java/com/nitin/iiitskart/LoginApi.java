package com.nitin.iiitskart;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonObject;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;
import retrofit2.http.Body;
import retrofit2.http.Headers;
import retrofit2.http.POST;

public class LoginApi {
    private static Gson gson=new GsonBuilder().setLenient().create();
    private static  final String baseURL="http://192.168.43.39:8000/";
    private static final String Cart_url="cart/profilevalidationapi/";


    private static Retrofit retrofit=new Retrofit.Builder().baseUrl(baseURL).addConverterFactory(GsonConverterFactory.create(gson)).build();

    private  interface Validate{
        @Headers("Content-Type: application/json")
        @POST(Cart_url)
        Call<JsonObject> validate(@Body Login_class login_class);
    }

    public  static void validate(Login_class login_class, Callback<JsonObject> callback){
        Validate validateApi=retrofit.create(Validate.class);
        Call<JsonObject> call=validateApi.validate(login_class);
        call.enqueue(callback);
    }
}
