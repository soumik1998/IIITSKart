package com.nitin.iiitskart;

import android.content.Intent;
import android.os.Bundle;
import android.app.Activity;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import com.google.gson.Gson;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;

import java.util.ArrayList;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class profilePageOwn extends Activity {
    String Username;
    TextView phoneText;
    TextView usernameText;
    TextView addressText;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_profile_page_own);
        Username= getIntent().getStringExtra("Username");
        usernameText=findViewById(R.id.nameTextView);
        phoneText=findViewById(R.id.phoneTextView);
        addressText=findViewById(R.id.locationTextView);
        usernameText.setText(Username.toUpperCase());
        getApi.getCustDetails(Username, new Callback<JsonObject>() {
            @Override
            public void onResponse(Call<JsonObject> call, Response<JsonObject> response) {
                final ArrayList<String> ratingArrayList = new ArrayList<String>();
                final ArrayList<String>  textArrayList = new ArrayList<String>();

                Log.i("Soumik",response.toString());
                JsonObject res=response.body();
                Customer customerObj = new Gson().fromJson(res, Customer.class);
                Log.e("Nitinwa",customerObj.getPhone());
                Log.e("Nitinwa",customerObj.getAddress());

                phoneText.setText(customerObj.getPhone());
                addressText.setText(customerObj.getAddress());
                Log.e("Nitinwa",customerObj.getAddress());

                JsonArray jsonArray = res.getAsJsonArray("result");
                for (JsonElement jsonElement : jsonArray) {
                    JsonObject product = jsonElement.getAsJsonObject();
                    C_review creviewObj = new Gson().fromJson(product, C_review.class);
                    Log.i("Nitinwa1",creviewObj.text);
                    ratingArrayList.add(creviewObj.rating);
                    textArrayList.add(creviewObj.text);
                }
                final String[] ratingArray=ratingArrayList.toArray(new String[ratingArrayList.size()]);

                final String[] textArray=textArrayList.toArray(new String[textArrayList.size()]);

                Log.i("Nitinwa",ratingArray.toString());
                Log.i("Nitinwa",textArray.toString());
                ListView listView=findViewById(R.id.listViewReview);
                CustomListReview adapter=new CustomListReview(  profilePageOwn.this,ratingArray,textArray);
                listView.setAdapter(adapter);
                listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
                    @Override
                    public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                        Toast.makeText(profilePageOwn .this,"You Clicked at " + ratingArray[+ position], Toast.LENGTH_SHORT).show();

                    }
                });

            }

            @Override
            public void onFailure(Call<JsonObject> call, Throwable t) {
                Log.e("Soumik",t.toString());
            }
        });


    }
    public void show_orders(View view){
        Intent myIntent = new Intent(this,OrderedProducts.class);
        myIntent.putExtra("Username",Username);
        startActivity(myIntent);

    }

}


