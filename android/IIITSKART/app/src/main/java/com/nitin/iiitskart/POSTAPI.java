package com.nitin.iiitskart;

import android.net.Uri;
import android.util.Log;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonObject;

import java.io.File;
import java.io.StringReader;

import okhttp3.RequestBody;
import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;
import retrofit2.http.Body;
import retrofit2.http.Headers;
import retrofit2.http.Multipart;
import retrofit2.http.POST;
import retrofit2.http.Part;

public class POSTAPI {
    private static final String baseUrl = "http://192.168.43.39:8000/";
    private static final String Cart_url = "cart/receive/";


    private interface AddCustomerReviewAPI {

        @Headers("Content-Type: application/json")
        @POST("cart/seller_reviewApi/")
        Call<JsonObject> addCustomerReview(@Body C_review c_review);
    }

    public static void addCustomerReview(C_review c_review, Callback<JsonObject> callback) {
        Gson gson = new GsonBuilder().setLenient().create();
        Retrofit retrofit = new Retrofit.Builder().baseUrl(baseUrl).addConverterFactory(GsonConverterFactory.create(gson)).build();
        AddCustomerReviewAPI addCustomerReviewAPI = retrofit.create(AddCustomerReviewAPI.class);
        Call<JsonObject> call = addCustomerReviewAPI.addCustomerReview(c_review);
        call.enqueue(callback);
    }

    private interface AddProductReviewAPI {

        @Headers("Content-Type: application/json")
        @POST("cart/product_reviewApi/")
        Call<JsonObject> addProductReview(@Body ProductReview productReview);
    }

    public static void addProductReview(ProductReview productReview, Callback<JsonObject> callback) {
        Gson gson = new GsonBuilder().setLenient().create();
        Retrofit retrofit = new Retrofit.Builder().baseUrl(baseUrl).addConverterFactory(GsonConverterFactory.create(gson)).build();
        AddProductReviewAPI addProductReviewAPI = retrofit.create(AddProductReviewAPI.class);
        Call<JsonObject> call = addProductReviewAPI.addProductReview(productReview);
        call.enqueue(callback);
    }

    private interface BuyApi {

        @Headers("Content-Type: application/json")
        @POST("cart/buy_Api/")
        Call<JsonObject> buy_pro(@Body OrderClass orderClass);
    }

    public static void buy_pro(OrderClass orderClass, Callback<JsonObject> callback) {
        Gson gson = new GsonBuilder().setLenient().create();
        Retrofit retrofit = new Retrofit.Builder().baseUrl(baseUrl).addConverterFactory(GsonConverterFactory.create(gson)).build();
        BuyApi buyApi = retrofit.create(BuyApi.class);
        Call<JsonObject> call = buyApi.buy_pro(orderClass);
        call.enqueue(callback);
    }
}


