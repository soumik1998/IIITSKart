package com.nitin.iiitskart;

import android.app.Dialog;
import android.content.Intent;
import android.os.Bundle;
import android.app.Activity;
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

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class profile_user extends Activity {

    String username;
    String seller_username;
    TextView phoneText;
    TextView usernameText;
    TextView addressText;

    String pop_review;
    String pop_rating;
    Spinner popup_rating_spinner;
    EditText popup_review_editText;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_profile_user);
        phoneText=findViewById(R.id.phoneTextView);
        usernameText=findViewById(R.id.nameTextView);
        addressText=findViewById(R.id.locationTextView);


        username= getIntent().getStringExtra("Username");
        seller_username=getIntent().getStringExtra("Seller_username");

        Log.i("Nitin12",username+seller_username);

        getApi.getCustDetails(seller_username, new Callback<JsonObject>() {
            @Override
            public void onResponse(Call<JsonObject> call, Response<JsonObject> response) {
                final ArrayList<String> ratingArrayList = new ArrayList<String>();
                final ArrayList<String>  textArrayList = new ArrayList<String>();

                JsonObject res=response.body();
                Customer customerObj = new Gson().fromJson(res, Customer.class);
                Log.i("NitinwaAddress",customerObj.getAddress());
                phoneText.setText(customerObj.getPhone());
                addressText.setText(customerObj.getAddress());
                usernameText.setText(customerObj.getUsername().toUpperCase());
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
                CustomListReview adapter=new CustomListReview(  profile_user.this,ratingArray,textArray);
                listView.setAdapter(adapter);
                listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
                    @Override
                    public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                        Toast.makeText(profile_user .this,"You Clicked at " + ratingArray[+ position], Toast.LENGTH_SHORT).show();

                    }
                });

            }

            @Override
            public void onFailure(Call<JsonObject> call, Throwable t) {
                Log.e("Nitinwa",t.toString());
            }
        });


    }

    public void callLoginDialog(View view)
    {
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
                sendReviewToserver(seller_username,pop_rating,pop_review);
                Log.i("Seller_srname",seller_username);
                //your login calculation goes here
            }
        });

    }
    void sendReviewToserver(String seller_username,String pop_rating,String pop_review){
        POSTAPI.addCustomerReview(new C_review(pop_rating,pop_review,username,seller_username), new Callback<JsonObject>() {
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

    public void Chat(View view){
        Intent myIntent = new Intent(profile_user.this, chat.class);
        myIntent.putExtra("Username",username);
        myIntent.putExtra("Seller_username",seller_username);
        startActivity(myIntent);
    }

}
