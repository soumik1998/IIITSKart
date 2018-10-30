package com.nitin.iiitskart;

import android.content.Intent;
import android.graphics.Bitmap;
import android.net.Uri;
import android.os.Bundle;
import android.app.Activity;
import android.provider.MediaStore;
import android.util.Base64;
import android.util.Log;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.Spinner;

import com.google.gson.JsonObject;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.util.ArrayList;

import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class sellProduct extends Activity {
    ImageView imageView;
    private static int IMAGE_REQUEST_CODE = 123;
    private static Uri filePath;
    Bitmap bitmap;
    Spinner spinnerQuant;
    EditText price;
    EditText description;
    EditText title;
    Spinner spinnerCat;
    String Username;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_sell_product);

        Username = getIntent().getStringExtra("Username");


        imageView = findViewById(R.id.imageUpload);
        spinnerQuant = (Spinner) findViewById(R.id.spinnerQuantity);
        spinnerCat = (Spinner) findViewById(R.id.spinnerCategory);
        price = findViewById(R.id.priceTextView);
        description = findViewById(R.id.descriptionText);
        title = findViewById(R.id.titleText);
        initializeSpinner();
        Log.e("Nitinwa1", Username);


    }

    public void postRequest(View view) {
        Log.e("Nitinwa", (String) spinnerCat.getSelectedItem());
        Log.e("Nitinwa", (String) spinnerQuant.getSelectedItem());
        Log.e("Nitinwa1", Username);
        String Category = spinnerCat.getSelectedItem().toString();
        int Quantity = Integer.parseInt(spinnerQuant.getSelectedItem().toString());
        String Title = title.getText().toString();
        String Description = description.getText().toString();
        float Price = Float.parseFloat(price.getText().toString());

        postApiTables.addProduct(new ProductClass(Title, Description, Category, Quantity, Price, Username,imageToString(bitmap),filePath.toString()), new Callback<JsonObject>() {
            @Override
            public void onResponse(Call<JsonObject> call, Response<JsonObject> response) {
                Log.i("NitinwaResponse", response.toString());

            }

            @Override
            public void onFailure(Call<JsonObject> call, Throwable t) {
                Log.e("NitinwaResponse", t.getMessage().toString());

            }

        });

    }

    void initializeSpinner() {
        ArrayList<String> qunatity = new ArrayList<String>();
        for (int i = 1; i <= 100; i++) {
            qunatity.add(Integer.toString(i));
        }
        ArrayAdapter<String> spinnerArrayAdapter = new ArrayAdapter<String>(
                this, android.R.layout.simple_spinner_item, qunatity);
        spinnerArrayAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);

        spinnerQuant.setAdapter(spinnerArrayAdapter);


    }

    public void upload(View view) {
        Intent intent = new Intent();
        intent.setType("image/*");
        intent.setAction(Intent.ACTION_GET_CONTENT);
        startActivityForResult(Intent.createChooser(intent, "Complete action using"), IMAGE_REQUEST_CODE);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        if (requestCode == IMAGE_REQUEST_CODE && resultCode == RESULT_OK && data != null && data.getData() != null) {
            filePath = data.getData();
            try {
                bitmap = MediaStore.Images.Media.getBitmap(getContentResolver(), filePath);
                imageView.setImageBitmap(bitmap);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }


    private String imageToString(Bitmap bitmap) {
        ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream();
        bitmap.compress(Bitmap.CompressFormat.JPEG, 100, byteArrayOutputStream);
        byte[] imgBytes=byteArrayOutputStream.toByteArray();
        return imgBytes.toString();
    }




}
