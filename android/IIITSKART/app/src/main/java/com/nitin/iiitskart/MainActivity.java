package com.nitin.iiitskart;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.preference.PreferenceManager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class MainActivity extends AppCompatActivity {
    String username;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        username= getIntent().getStringExtra("Username");
    }

    public void show_Products(View view){
        Intent myIntent = new Intent(this, Buy.class);
        myIntent.putExtra("Username",username);

        startActivity(myIntent);
    }
    public void show_user(View view){
        Intent myIntent = new Intent(this, profilePageOwn.class);
        myIntent.putExtra("Username",username);
        startActivity(myIntent);
    }
    public void postAd(View view){
        Intent myIntent = new Intent(this, sellProduct.class);
        myIntent.putExtra("Username",username);
        startActivity(myIntent);
    }

    public void Logout(View view){
        SharedPreferences settings = getSharedPreferences("userinfo", Context.MODE_PRIVATE);
        settings.edit().clear().commit();
        Intent myIntent = new Intent(this, Login.class);
        startActivity(myIntent);
    }

    public void showMessages(View view){
        Intent myIntent = new Intent(this, Chat_member.class);
        myIntent.putExtra("Username",username);
        startActivity(myIntent);
    }
}
