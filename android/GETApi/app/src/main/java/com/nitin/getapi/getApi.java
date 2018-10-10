package com.nitin.getapi;

import retrofit2.Retrofit;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonObject;
import com.google.gson.JsonParseException;
import com.google.gson.JsonPrimitive;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;
import retrofit2.http.Body;
import retrofit2.http.GET;
import retrofit2.http.Headers;
import retrofit2.http.POST;
import retrofit2.http.Query;


public class getApi {


    private static Gson gson = new GsonBuilder().setLenient().create();
    private static final String baseUrl="http://192.168.43.39:8000/";
    private static final String Cart_url="cart/receive/";


    private static Retrofit retrofit=new Retrofit.Builder().baseUrl(baseUrl).addConverterFactory(GsonConverterFactory.create(gson)).build();

    private interface AddCustomerAPI{

        @Headers("Content-Type: application/json")
        @GET("cart/send/")
        Call<JsonObject> getList(@Query("class_name") String class_name);
    }
    public static void getList(String class_name,Callback<JsonObject> callback ){

        AddCustomerAPI addCustomerAPI=retrofit.create(AddCustomerAPI.class);
        Call<JsonObject> call = addCustomerAPI.getList(class_name);
        call.enqueue(callback);
    }
}

