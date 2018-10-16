package com.nitin.iiitskart;

import android.content.Intent;
import android.os.Bundle;
import android.app.Activity;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

import com.google.gson.JsonElement;
import com.google.gson.JsonObject;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class Login extends Activity {
    EditText userName;
    EditText Password;
    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
        userName=findViewById(R.id.userEditText);
        Password=findViewById(R.id.passEditText);

    }

    public void Sign_up(View view){
        String username=userName.getText().toString();
        String password=Password.getText().toString();

        LoginApi.validate(new Login_class(username, password), new Callback<JsonObject>() {
            @Override
            public void onResponse(Call<JsonObject> call, Response<JsonObject> response) {
                JsonObject res=response.body();
                String resp=res.get("status").toString();
                String resp1=resp.substring(1,resp.length()-1);
                Log.e("Nitinwa", resp1);

                if(resp1.equals("Yes")){
                    Log.i("Nitinwa","fgggggggggggggggggggggd");
                    Toast.makeText(getApplicationContext(),"Logged IN",Toast.LENGTH_LONG).show();
                    Intent intent = new Intent(Login.this, MainActivity.class);
                    startActivity(intent);

                }
                if(resp1.equals("No")){
                    Toast.makeText(getApplicationContext(),"Invalid credentials",Toast.LENGTH_LONG).show();
                }
//                if(resp=="Error"){
//                    Toast.makeText(getApplicationContext(),"Error Occured",Toast.LENGTH_LONG).show();
//                }
//
            }

            @Override
            public void onFailure(Call<JsonObject> call, Throwable t) {
                Log.e("Nitin error",t.toString());
            }
        });
    }

}
