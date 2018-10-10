package com.nitin.getapi;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;

import com.google.gson.Gson;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import com.google.gson.JsonPrimitive;
import com.google.gson.reflect.TypeToken;

import java.lang.reflect.Type;
import java.util.ArrayList;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class MainActivity extends AppCompatActivity {

    private static final String TAG = MainActivity.class.toString();
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


    }
    public void onButtonPress(View view){

        String query_table="Customer";
        getApi.getList(query_table, new Callback<JsonObject>() {
            @Override
            public void onResponse(Call<JsonObject> call, Response<JsonObject> response) {
//                Log.i(MainActivity.class.toString(), response.body().toString());
                JsonObject res = response.body();
                JsonArray jsonArray = res.getAsJsonArray("data");
                for(JsonElement jsonElement: jsonArray) {
                    JsonObject jsonObject = jsonElement.getAsJsonObject();
                    JsonObject customer = jsonObject.getAsJsonObject("fields");
//                    Log.i(MainActivity.class.toString(), customer.toString());

                    Customer customerObj = new Gson().fromJson(customer, Customer.class);
                    Log.i(MainActivity.class.toString(), customerObj.getFirst_name());
                }
            }

            @Override
            public void onFailure(Call<JsonObject> call, Throwable t) {
                Log.e(MainActivity.class.toString(), t.getMessage());
            }
        });
    }
}
