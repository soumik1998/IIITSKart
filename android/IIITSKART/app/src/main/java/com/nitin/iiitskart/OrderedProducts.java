package com.nitin.iiitskart;

import android.content.Intent;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.design.widget.BottomNavigationView;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.MenuItem;
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
import java.util.TimerTask;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class OrderedProducts extends AppCompatActivity {
    String username;
    String Tag="Debug";
    private TextView mTextMessage;
    final ArrayList<OrderClass> OrderList_Buyer = new ArrayList<OrderClass>();
    final ArrayList<OrderClass> OrderList_Seller = new ArrayList<OrderClass>();
    final ArrayList<String> TitleList_Buyer = new ArrayList<String>();
    final ArrayList<String> TitleList_Seller = new ArrayList<String>();

    OrderClass[] orderArray_Buyer;
    OrderClass[] orderArray_Seller;
    String[] title_array_Buyer;
    String[] title_array_Seller;

    Integer[] imageId = {
            R.drawable.photo,
            R.drawable.pin,
            R.drawable.ball,
            R.drawable.bicycle,
            R.drawable.focus,
            R.drawable.laptop,
            R.drawable.book

    };
    ListView listView;
    private BottomNavigationView.OnNavigationItemSelectedListener mOnNavigationItemSelectedListener
            = new BottomNavigationView.OnNavigationItemSelectedListener() {

        @Override
        public boolean onNavigationItemSelected(@NonNull MenuItem item) {
            switch (item.getItemId()) {
                case R.id.navigation_bought:
                    if(OrderList_Buyer.size()!=0){
                        listView.setVisibility(View.VISIBLE);
                        createListView(title_array_Buyer,orderArray_Buyer);
                        mTextMessage.setText("Bought Products:");
                    }
                    else{
                        listView.setVisibility(View.INVISIBLE);
                        mTextMessage.setText("No Products Bought yet!");
                    }

                    Log.i("Test","Bought");
                    return true;

                case R.id.navigation_sold:
                    Log.i(Tag,title_array_Seller[0]);
                    if(OrderList_Seller.size()!=0){
                        listView.setVisibility(View.VISIBLE);
                        createListView(title_array_Seller,orderArray_Seller);
                        mTextMessage.setText("Sold Products:");
                    }
                    else{
                        listView.setVisibility(View.INVISIBLE);
                        mTextMessage.setText("No Products Sold yet!");
                    }

                    return true;
            }
            return false;
        }
    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_ordered_products);
        listView = (ListView) findViewById(R.id.listView_Orders);
        username= getIntent().getStringExtra("Username");
        getOrderInfo(username);

        mTextMessage = (TextView) findViewById(R.id.message);
        BottomNavigationView navigation = (BottomNavigationView) findViewById(R.id.navigation);
        navigation.setOnNavigationItemSelectedListener(mOnNavigationItemSelectedListener);


    }

    public void getOrderInfo(final String username){
        getApi.getOrderDetails(username, new Callback<JsonObject>() {
            @Override
            public void onResponse(Call<JsonObject> call, Response<JsonObject> response) {
                JsonObject res = response.body();
                Log.e("Chinmaya1",res.toString());

                JsonArray jsonArray = res.getAsJsonArray("result");
                for (JsonElement jsonElement : jsonArray) {
                    JsonObject product = jsonElement.getAsJsonObject();

                    Log.i("Chinmaya1",product.toString());
                    OrderClass orderObj = new Gson().fromJson(product, OrderClass.class);
                    if(orderObj.getBuyer().equals(username)){
                        OrderList_Buyer.add(orderObj);
                        TitleList_Buyer.add(orderObj.getProduct());
                    }
                    if(orderObj.getSellername().equals(username)) {
                        Log.i(Tag+"1",username+orderObj.getSellername());

                        OrderList_Seller.add(orderObj);
                        TitleList_Seller.add(orderObj.getProduct());
                    }
                }

                orderArray_Buyer=OrderList_Buyer.toArray(new OrderClass[OrderList_Buyer.size()]);
                orderArray_Seller=OrderList_Seller.toArray(new OrderClass[OrderList_Seller.size()]);
                title_array_Buyer=TitleList_Buyer.toArray(new String[TitleList_Buyer.size()]);
                title_array_Seller=TitleList_Seller.toArray(new String[TitleList_Seller.size()]);

                if(OrderList_Buyer.size()!=0){
                   createListView(title_array_Buyer,orderArray_Buyer);
                    mTextMessage.setText("Bought Products:");
                }
                else{
                    mTextMessage.setText("No Products Sold yet!");
                }
            }

            @Override
            public void onFailure(Call<JsonObject> call, Throwable t) {

            }
        });
    }

    public void createListView(String [] title_array,final OrderClass[] orderArray)
    {

        Log.i(Tag+"2",orderArray[0].getProduct()+title_array[0]);

        CustomList_order adapter = new CustomList_order(OrderedProducts.this, title_array,imageId);
        listView.setAdapter(adapter);

        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                Toast.makeText(OrderedProducts.this, "You Clicked at " + orderArray[+ position].getProduct(), Toast.LENGTH_SHORT).show();
//                Intent myIntent = new Intent(OrderedProducts.this, productPage.class);
//
//                myIntent.putExtra("Buyer",orderArray[+ position].getBuyer());
//                myIntent.putExtra("Seller_Username",orderArray[+ position].getSellername());
//                myIntent.putExtra("Date",orderArray[+position].getDate());
//                myIntent.putExtra("Product",orderArray[+position].getProduct());
//                startActivity(myIntent);
            }
        });


    }



}
