package com.nitin.iiitskart;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonObject;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;
import retrofit2.http.GET;
import retrofit2.http.Headers;
import retrofit2.http.Query;

public class getApi {

    private static Gson gson=new GsonBuilder().setLenient().create();
    private static final String baseUrl="http://192.168.43.39:8000/";

    //Adding the list of product
    private interface AddCustomerAPI {
        @Headers("Content-Type:application/json")
        @GET("cart/get_pro/")
        Call<JsonObject> getList();
    }
    public static void getList(Callback<JsonObject> callback ){

        final String Cart_url="cart/receive/";
        Retrofit retrofit=new Retrofit.Builder().baseUrl(baseUrl).addConverterFactory(GsonConverterFactory.create(gson)).build();
        AddCustomerAPI addCustomerAPI=retrofit.create(AddCustomerAPI.class);
        Call<JsonObject> call = addCustomerAPI.getList();
        call.enqueue(callback);
    }
//-----------------------------------------------------------------
    //Retrieving the customer Details
    private interface GetCustomerDetailAPI {
        @Headers("Content-Type:application/json")
        @GET("cart/get_user/")
        Call<JsonObject> getCustDetails(@Query("seller_usernamename") String seller_username);
    }
    public static void getCustDetails(String seller_username,Callback<JsonObject> callback ){

        final String Cart_url="cart/receive/";
        Retrofit retrofit=new Retrofit.Builder().baseUrl(baseUrl).addConverterFactory(GsonConverterFactory.create(gson)).build();
        GetCustomerDetailAPI getCustomerDetailAPI=retrofit.create(GetCustomerDetailAPI.class);
        Call<JsonObject> call = getCustomerDetailAPI.getCustDetails(seller_username);
        call.enqueue(callback);
    }
}
