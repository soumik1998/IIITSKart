package com.nitin.iiitskart;

import android.app.Dialog;
import android.content.Intent;
import android.net.wifi.p2p.WifiP2pManager;
import android.os.Bundle;
import android.app.Activity;
import android.support.design.widget.Snackbar;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Toast;

import com.google.gson.Gson;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;

import java.util.ArrayList;
import java.util.List;
import java.util.Timer;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class productPage extends Activity {

    String title;
    int quantity;
    String description;
    Float price;
    String category;
    String username;
    String seller_username;
    TextView nameText;
    TextView priceText;
    TextView descriptionText;
    TextView titleText;
    String pop_review;
    String pop_rating;
    Spinner spinnerQuant;
    Spinner popup_rating_spinner;
    EditText popup_review_editText;
    ListView listViewProductReview;
    Button review_buton;
    Button buy_buton;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_product_page);
        review_buton=findViewById(R.id.ReviewButton);
        buy_buton=findViewById(R.id.buyButton);
        listViewProductReview=findViewById(R.id.listViewProductReview);
        spinnerQuant=findViewById(R.id.spinnerQuant);
        username= getIntent().getStringExtra("Username");
        price= getIntent().getFloatExtra("Price", (float) 0.0);
        title= getIntent().getStringExtra("Title");
        category=getIntent().getStringExtra("Category");
        seller_username= getIntent().getStringExtra("Seller_Username");
        description=getIntent().getStringExtra("Description");
        quantity=getIntent().getIntExtra("Quantity",1);
        initializeSpinner_Quntity();
        nameText=findViewById(R.id.nameTextView);
        priceText=findViewById(R.id.priceTextView);
        descriptionText=findViewById(R.id.descriptionText);
        titleText=findViewById(R.id.titleText);
                nameText.setText(seller_username.toUpperCase());
                priceText.setText(price.toString());
                descriptionText.setText(description);
                titleText.setText(title);

        makeListReview();
    }
    void  makeListReview(){
        getApi.getProReview(seller_username,title, new Callback<JsonObject>() {
            @Override
            public void onResponse(Call<JsonObject> call, Response<JsonObject> response) {
                final ArrayList<String> ratingArrayList = new ArrayList<String>();
                final ArrayList<String>  textArrayList = new ArrayList<String>();

                JsonObject res=response.body();
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
                CustomListReview adapter=new CustomListReview(  productPage.this,ratingArray,textArray);
                listViewProductReview.setAdapter(adapter);
                listViewProductReview.setOnItemClickListener(new AdapterView.OnItemClickListener() {
                    @Override
                    public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                        Toast.makeText(productPage.this,"You Clicked at " + ratingArray[+ position], Toast.LENGTH_SHORT).show();
                    }
                });

            }

            @Override
            public void onFailure(Call<JsonObject> call, Throwable t) {
                Log.e("Nitinwa",t.toString());
            }
        });
    }
    public  void showuser(View view){
        Intent myIntent = new Intent(productPage.this, profile_user.class);
        myIntent.putExtra("Username",username);
        myIntent.putExtra("Seller_username",seller_username);
        startActivity(myIntent);
    }
    public void reportUser(View view){

    }
    public void review(View view){
        final Dialog myDialog = new Dialog(this);
        myDialog.setContentView(R.layout.pop_up_review);

        Button submit = (Button) myDialog.findViewById(R.id.submit);
        TextView rate=myDialog.findViewById(R.id.RATE);
        String rate_string="Rate "+seller_username;
        rate.setText(rate_string);
        popup_rating_spinner = myDialog.findViewById(R.id.rating);
        popup_review_editText = (EditText) myDialog.findViewById(R.id.reviewText);
        initializeSpinner();
        myDialog.show();

        submit.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                pop_rating=popup_rating_spinner.getSelectedItem().toString();
                pop_review=popup_review_editText.getText().toString();
                myDialog.dismiss();
                sendProductReviewToserver(seller_username,title,pop_rating,pop_review);
                Log.i("Seller_srname",seller_username);
                //your login calculation goes here
            }
        });

    }

    void sendProductReviewToserver(String seller_username,String title,String pop_rating,String pop_review){
        POSTAPI.addProductReview(new ProductReview(pop_rating,pop_review,title,seller_username), new Callback<JsonObject>() {
            @Override
            public void onResponse(Call<JsonObject> call, Response<JsonObject> response) {
                Log.i(getClass().toString(),response.toString());
            }

            @Override
            public void onFailure(Call<JsonObject> call, Throwable t) {
                Log.e(getClass().toString(),t.getMessage().toString());
            }
        });

    }

    void initializeSpinner(){
        ArrayList<String> qunatity = new ArrayList<String>();
        for (int i = 1; i <= 5; i++) {
            qunatity.add(Integer.toString(i));
        }

        ArrayAdapter<String> spinnerArrayAdapter = new ArrayAdapter<String>(
                this, android.R.layout.simple_spinner_item, qunatity);
        spinnerArrayAdapter.setDropDownViewResource( android.R.layout.simple_spinner_dropdown_item );

        popup_rating_spinner.setAdapter(spinnerArrayAdapter);


    }

    void initializeSpinner_Quntity(){
        ArrayList<String> qunatity = new ArrayList<String>();
        for (int i = 1; i <= quantity; i++) {
            qunatity.add(Integer.toString(i));
        }

        ArrayAdapter<String> spinnerArrayAdapter = new ArrayAdapter<String>(
                this, android.R.layout.simple_spinner_item, qunatity);
        spinnerArrayAdapter.setDropDownViewResource( android.R.layout.simple_spinner_dropdown_item );

        spinnerQuant.setAdapter(spinnerArrayAdapter);


    }

    public  void buy_button(View view){
        String total_amt= String.valueOf(price*quantity);
        POSTAPI.buy_pro(new OrderClass(title, username, seller_username, String.valueOf(quantity), total_amt, String.valueOf(price)), new Callback<JsonObject>() {
            @Override
            public void onResponse(Call<JsonObject> call, Response<JsonObject> response) {
                review_buton.setVisibility(View.INVISIBLE);
                buy_buton.setVisibility(View.INVISIBLE);
                Snackbar.make(findViewById(R.id.myCoordinatorLayout), R.string.email_sent,
                        Snackbar.LENGTH_SHORT)
                        .show();
            }


            @Override
            public void onFailure(Call<JsonObject> call, Throwable t) {

            }
        });
    }
}
