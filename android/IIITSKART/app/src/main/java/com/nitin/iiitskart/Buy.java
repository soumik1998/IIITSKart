package com.nitin.iiitskart;

import android.content.Intent;
import android.os.Bundle;
import android.app.Activity;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ListView;
import android.widget.Toast;

import com.google.gson.Gson;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;

import java.util.ArrayList;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class Buy extends Activity {
    String username;
    Integer[] imageId = {
            R.drawable.photo,
            R.drawable.pin,
            R.drawable.ball,
            R.drawable.bicycle,
            R.drawable.focus,
            R.drawable.laptop,
            R.drawable.book

    };
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_buy);
        username= getIntent().getStringExtra("Username");

        Log.i("Chinmaya1", "asdasdbajg");

        getApi.getList(new Callback<JsonObject>() {
            @Override
            public void onResponse(Call<JsonObject> call, Response<JsonObject> response) {
                final ArrayList<String>  stringArray = new ArrayList<String>();
                final ArrayList<ProductClass>  ProductArrayList = new ArrayList<ProductClass>();

                JsonObject res = response.body();
                Log.e("Chinmaya1",res.toString());

                JsonArray jsonArray = res.getAsJsonArray("result");
                for (JsonElement jsonElement : jsonArray) {
                    JsonObject product = jsonElement.getAsJsonObject();

                    Log.i("Chinmaya1",product.toString());
                    ProductClass productObj = new Gson().fromJson(product, ProductClass.class);
                   Log.i("Chinmaya1", productObj.getTitle()+productObj.getUsername());

                    stringArray.add(productObj.getTitle());
                    ProductArrayList.add(productObj);
                }





                final String[] array = stringArray.toArray(new String[stringArray.size()]);
                final ProductClass[] productArray=ProductArrayList.toArray(new ProductClass[ProductArrayList.size()]);
                ListView listView = (ListView) findViewById(R.id.listViewReview);
                CustomList adapter = new CustomList(Buy.this, array,imageId);
                listView.setAdapter(adapter);

                listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
                    @Override
                    public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                        Toast.makeText(Buy.this, "You Clicked at " + productArray[+ position].getPrice(), Toast.LENGTH_SHORT).show();
                        Intent myIntent = new Intent(Buy.this, productPage.class);

                        myIntent.putExtra("Username",username);
                        myIntent.putExtra("Seller_Username",productArray[+ position].getUsername());
                        myIntent.putExtra("Title",productArray[+ position].getTitle());
                        myIntent.putExtra("Description",productArray[+ position].getDescription());
                        myIntent.putExtra("Category",productArray[+ position].getCategory());
                        myIntent.putExtra("Quantity",productArray[+ position].getQuantity());
                        myIntent.putExtra("Price",productArray[+ position].getPrice());
                        startActivity(myIntent);
                    }
                });


            }



            @Override
            public void onFailure(Call<JsonObject> call, Throwable t) {
                    Log.i(getClass().toString(),t.toString());
            }});



    }

}
