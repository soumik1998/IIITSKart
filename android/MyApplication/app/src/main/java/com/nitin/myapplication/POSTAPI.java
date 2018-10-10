package com.nitin.myapplication;

import retrofit2.Retrofit;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonObject;
import com.nitin.myapplication.Class.Customer;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.converter.gson.GsonConverterFactory;
import retrofit2.http.Body;
import retrofit2.http.Headers;
import retrofit2.http.POST;


public class POSTAPI {


    private static Gson gson = new GsonBuilder().setLenient().create();
    private static final String baseUrl="http://192.168.43.39:8000/";
    private static final String Cart_url="cart/receive/";


    private static Retrofit retrofit=new Retrofit.Builder().baseUrl(baseUrl).addConverterFactory(GsonConverterFactory.create(gson)).build();

    private interface AddCustomerAPI{

        @Headers("Content-Type: application/json")
        @POST("cart/receive/")
        Call<JsonObject> addCustomer(@Body Customer customer);
    }
    public static void addCustomer(Customer customer,Callback<JsonObject> callback ){
        AddCustomerAPI addCustomerAPI=retrofit.create(AddCustomerAPI.class);
        Call<JsonObject> call=addCustomerAPI.addCustomer(customer);
        call.enqueue(callback);

    }
}
