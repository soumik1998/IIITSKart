package com.nitin.iiitskart;

import android.app.Activity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ImageView;
import android.widget.TextView;


    public class CustomListReview extends ArrayAdapter<String> {

        private final Activity context;
        private final String[] text;
        private final String[] rating;
        public CustomListReview(Activity context,
                          String[] rating, String[] text) {
            super(context, R.layout.list_twoitems,text );
            this.context = context;
            this.rating = rating;
            this.text = text;

        }
        @Override
        public View getView(int position, View view, ViewGroup parent) {
            LayoutInflater inflater = context.getLayoutInflater();
            View rowView= inflater.inflate(R.layout.list_twoitems, null, true);
            TextView txtTitle = (TextView) rowView.findViewById(R.id.txt);

            TextView ratingView = (TextView)rowView.findViewById(R.id.rating);
            txtTitle.setText(text[position]);
            ratingView.setText(rating[position]);
            return rowView;
        }
    }

