package com.nitin.iiitskart;

import android.net.Uri;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonObject;

import org.json.JSONObject;

import java.io.File;

import okhttp3.MediaType;
import okhttp3.MultipartBody;
import okhttp3.OkHttpClient;
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

public class postApiTables {
    private static Gson gson = new GsonBuilder().setLenient().create();
    private static final String baseUrl="http://192.168.43.39:8000/";
    private static final String Cart_url="cart/receive/";


    private static Retrofit retrofit=new Retrofit.Builder().baseUrl(baseUrl).addConverterFactory(GsonConverterFactory.create(gson)).build();

    private  interface AddProductAPI{
        @Headers("Content-Type: application/json")
        @POST("cart/receiveProduct/")
        Call<JsonObject> addProduct(@Body ProductClass productClass);
    }
    public static void addProduct(ProductClass productClass, Callback<JsonObject> callback){
        AddProductAPI addProductAPI=retrofit.create(AddProductAPI.class);
        Call<JsonObject> call=addProductAPI.addProduct(productClass);
        call.enqueue(callback);
    }
   }


