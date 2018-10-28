package com.nitin.iiitskart;

import android.content.Context;
import android.content.SharedPreferences;
import android.support.design.widget.FloatingActionButton;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.text.format.DateFormat;
import android.util.Log;
import android.view.Menu;
import android.view.View;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.TextView;

import com.firebase.ui.database.FirebaseListAdapter;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

public class chat extends AppCompatActivity {
    private FirebaseListAdapter<ChatMessage> adapter;
    String username;
    String seller_username;
    String CONCAT;
    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_chat);
        username= getIntent().getStringExtra("Username").toLowerCase();
        seller_username=getIntent().getStringExtra("Seller_username").toLowerCase();




        Log.i("BIGGER",username+seller_username);
        int big=username.compareTo(seller_username);
        Log.i("Bigger",String.valueOf(big));
        if(big > 0)
            CONCAT=username+seller_username;
        else
            CONCAT=seller_username+username;
        final FirebaseDatabase database = FirebaseDatabase.getInstance();
        FloatingActionButton fab =
                (FloatingActionButton)findViewById(R.id.fab);
        displayChatMessages();
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                EditText input = (EditText)findViewById(R.id.input);

                // Read the input field and push a new instance
                // of ChatMessage to the Firebase database
                Log.i("NITINWA",input.getText().toString());
                DatabaseReference reference = database.getReference("Messages");
                DatabaseReference userRef=reference.child(CONCAT);
                userRef.push().setValue(new ChatMessage(input.getText().toString(),
                        username));

                    DatabaseReference reference1 = FirebaseDatabase.getInstance().getReference("User");
                    DatabaseReference userRef_user = reference1.child(username).child(seller_username);
                    userRef_user.setValue(seller_username);
                    DatabaseReference userRef_seller = reference1.child(seller_username).child(username);
                    userRef_seller.setValue(username);


                // Clear the input
                input.setText("");
                displayChatMessages();
            }
        });
    }
//
//    private boolean usernameExists(String username,String seller_username) {
//        DatabaseReference fdbRefer = FirebaseDatabase.getInstance().getReference("User/"+username+"/"+seller_username);
//        if(fdbRefer != null)
//            Log.i("Nitin","Exists");
//        else
//            Log.i("Nitin","Not Exists");
//        return (fdbRefer == null);
//    }

    void  displayChatMessages()
    {
    ListView listOfMessages = (ListView)findViewById(R.id.list_of_messages);

    adapter = new FirebaseListAdapter<ChatMessage>(this, ChatMessage.class, R.layout.message, FirebaseDatabase.getInstance().getReference("Messages").child(CONCAT)) {
        @Override
        protected void populateView(View v, ChatMessage model, int position) {
            // Get references to the views of message.xml
            TextView messageText = (TextView)v.findViewById(R.id.message_text);
            TextView messageUser = (TextView)v.findViewById(R.id.message_user);
            TextView messageTime = (TextView)v.findViewById(R.id.message_time);

            // Set their text
            messageText.setText(model.getMessageText());
            messageUser.setText(model.getMessageUser());

            // Format the date before showing it
            messageTime.setText(DateFormat.format("dd-MM-yyyy (HH:mm:ss)",
                    model.getMessageTime()));
        }
    };

listOfMessages.setAdapter(adapter);

}


}
