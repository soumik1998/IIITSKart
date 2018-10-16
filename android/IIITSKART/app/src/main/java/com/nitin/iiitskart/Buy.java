package com.nitin.iiitskart;

import android.os.Bundle;
import android.app.Activity;
import android.util.Log;
import android.widget.ArrayAdapter;
import android.widget.ListView;

import com.google.gson.Gson;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.nitin.iiitskart.classes.Customer;

import java.util.ArrayList;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class Buy extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_buy);
         String query_table="Customer";
        getApi.getList(query_table, new Callback<JsonObject>() {
            @Override
            public void onResponse(Call<JsonObject> call, Response<JsonObject> response) {
                ArrayList<String>  stringArray = new ArrayList<String>();

                JsonObject res = response.body();
                JsonArray jsonArray = res.getAsJsonArray("data");
                for (JsonElement jsonElement : jsonArray) {
                    JsonObject jsonObject = jsonElement.getAsJsonObject();
                    JsonObject customer = jsonObject.getAsJsonObject("fields");
//                    Log.i(MainActivity.class.toString(), customer.toString());

                    Customer customerObj = new Gson().fromJson(customer, Customer.class);
                    Log.i(getClass().toString(), customerObj.getFirst_name());
                }

                for (JsonElement jsonElement : jsonArray) {
                    stringArray.add(jsonElement.getAsJsonObject().toString());
                }
                ArrayAdapter<String> adapter = new ArrayAdapter<String>(Buy.this,android.R.layout.simple_list_item_1,stringArray);
                ListView listView = (ListView) findViewById(R.id.listView);
                listView.setAdapter(adapter);


            }



            @Override
            public void onFailure(Call<JsonObject> call, Throwable t) {
                    Log.i(getClass().toString(),t.toString());
            }});



    }

}
