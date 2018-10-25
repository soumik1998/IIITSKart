package com.nitin.iiitskart;

import android.content.Intent;
import android.os.Bundle;
import android.app.Activity;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Spinner;
import android.widget.TextView;

import java.util.ArrayList;
import java.util.List;

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

    }

}
