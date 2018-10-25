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
import okhttp3.logging.HttpLoggingInterceptor;
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
    public static void addProduct(Uri filePath,ProductClass productClass, Callback<JsonObject> callback){
        AddProductAPI addProductAPI=retrofit.create(AddProductAPI.class);
        Call<JsonObject> call=addProductAPI.addProduct(productClass);
        call.enqueue(callback);
    }
    private interface Service {
        @Multipart
        @POST("cart/receiveProduct/")
        Call<ResponseBody> postImage(@Part MultipartBody.Part image, @Part("name") RequestBody name);
    }


    public static void addPhotoApi(Uri filePath,Callback<ResponseBody> callback)
    {
        HttpLoggingInterceptor interceptor = new HttpLoggingInterceptor();
        interceptor.setLevel(HttpLoggingInterceptor.Level.BODY);
        OkHttpClient client = new OkHttpClient.Builder().addInterceptor(interceptor).build();

        Service service = new Retrofit.Builder().baseUrl(baseUrl).client(client).build().create(Service.class);

        File file = new File(filePath.getPath());

        RequestBody reqFile = RequestBody.create(MediaType.parse("image/*"), file);
        MultipartBody.Part body = MultipartBody.Part.createFormData("upload", file.getName(), reqFile);
        RequestBody name = RequestBody.create(MediaType.parse("text/plain"), "upload_test");

        retrofit2.Call<okhttp3.ResponseBody> req = service.postImage(body, name);
        req.enqueue(new Callback<ResponseBody>() {
            @Override
            public void onResponse(Call<ResponseBody> call, Response<ResponseBody> response) {
                // Do Something
            }

            @Override
            public void onFailure(Call<ResponseBody> call, Throwable t) {
                t.printStackTrace();
            }
        });

    }
}


