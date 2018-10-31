package com.nitin.iiitskart;

import android.app.Dialog;
import android.content.Intent;
import android.os.Bundle;
import android.app.Activity;
import android.util.Log;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.TextView;

import com.google.gson.JsonObject;

import java.util.ArrayList;
import java.util.List;

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
    Spinner popup_rating_spinner;
    EditText popup_review_editText;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_product_page);
        username= getIntent().getStringExtra("Username");
        price= getIntent().getFloatExtra("Price", (float) 0.0);
        title= getIntent().getStringExtra("Title");
        category=getIntent().getStringExtra("Category");
        seller_username= getIntent().getStringExtra("Seller_Username");
        description=getIntent().getStringExtra("Description");
        nameText=findViewById(R.id.nameTextView);
        priceText=findViewById(R.id.priceTextView);
        descriptionText=findViewById(R.id.descriptionText);
        titleText=findViewById(R.id.titleText);
                nameText.setText(seller_username.toUpperCase());
                priceText.setText(price.toString());
                descriptionText.setText(description);
                titleText.setText(title);
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

}
