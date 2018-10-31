package com.nitin.iiitskart;

import android.content.Intent;
import android.os.Bundle;
import android.app.Activity;
import android.text.format.DateFormat;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import com.firebase.ui.database.FirebaseListAdapter;
import com.google.firebase.database.FirebaseDatabase;
import com.google.gson.Gson;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;

import java.util.ArrayList;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class Chat_member extends Activity {
    private FirebaseListAdapter<UserIds> adapter;
    String username;
    String concat;
    String seller_username;
    ListView listOfMessages;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_chat_member);
        username = getIntent().getStringExtra("Username").toLowerCase();
        listOfMessages = (ListView) findViewById(R.id.listView_names);

        displaylist();
        listOfMessages.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                TextView textview_concat=(TextView)view.findViewById(R.id.m_concat);
                TextView textview_user=(TextView)view.findViewById(R.id.m_user);

                concat=textview_concat.getText().toString();
                seller_username=textview_user.getText().toString();
                Intent myIntent = new Intent(Chat_member.this, chat.class);
                myIntent.putExtra("Username",username);
                myIntent.putExtra("Seller_username",seller_username);
                startActivity(myIntent); }
        });
    }
    public void displaylist(){
        adapter = new FirebaseListAdapter<UserIds>(this, UserIds.class, R.layout.list_user, FirebaseDatabase.getInstance().getReference("User").child(username)) {
            @Override
            protected void populateView(View v, UserIds model, int position) {
                // Get references to the views of message.xml
                TextView messageText = (TextView)v.findViewById(R.id.m_text);
                TextView messageUser = (TextView)v.findViewById(R.id.m_user);
                TextView concat = (TextView)v.findViewById(R.id.m_concat);

                // Set their text
                messageText.setText(model.getLast_msg());
                messageUser.setText(model.getUser());
                concat.setText(model.getConcat());


                // Format the date before showing it
            }
        };

        listOfMessages.setAdapter(adapter);
    }
}
