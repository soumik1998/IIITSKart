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
        Call<JsonObject> getCustDetails(@Query("seller_username") String seller_username);
    }
    public static void getCustDetails(String seller_username,Callback<JsonObject> callback ){

        final String Cart_url="cart/receive/";
        Retrofit retrofit=new Retrofit.Builder().baseUrl(baseUrl).addConverterFactory(GsonConverterFactory.create(gson)).build();
        GetCustomerDetailAPI getCustomerDetailAPI=retrofit.create(GetCustomerDetailAPI.class);
        Call<JsonObject> call = getCustomerDetailAPI.getCustDetails(seller_username);
        call.enqueue(callback);
    }

    private interface GetOrderDetailAPI {
        @Headers("Content-Type:application/json")
        @GET("cart/get_order_detail/")
        Call<JsonObject> getOrderDetails(@Query("username") String username);
    }
    public static void getOrderDetails(String username,Callback<JsonObject> callback ){

        Retrofit retrofit=new Retrofit.Builder().baseUrl(baseUrl).addConverterFactory(GsonConverterFactory.create(gson)).build();
        GetOrderDetailAPI getOrderDetailAPI=retrofit.create(GetOrderDetailAPI.class);
        Call<JsonObject> call = getOrderDetailAPI.getOrderDetails(username);
        call.enqueue(callback);
    }

    private interface GetProductReviewAPI {
        @Headers("Content-Type:application/json")
        @GET("cart/get_productReview/")
        Call<JsonObject> getProReview(@Query("username") String username ,@Query("title") String title);
    }
    public static void getProReview(String username,String title,Callback<JsonObject> callback ){

        Retrofit retrofit=new Retrofit.Builder().baseUrl(baseUrl).addConverterFactory(GsonConverterFactory.create(gson)).build();
        GetProductReviewAPI getProductReviewAPI=retrofit.create(GetProductReviewAPI.class);
        Call<JsonObject> call = getProductReviewAPI.getProReview(username,title);
        call.enqueue(callback);
    }
}
