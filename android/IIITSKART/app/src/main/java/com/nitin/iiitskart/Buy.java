package com.nitin.iiitskart;

import android.content.Intent;
import android.os.Bundle;
import android.app.Activity;
import android.util.Log;
import android.view.MotionEvent;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.SearchView;
import android.widget.Spinner;
import android.widget.Toast;

import com.google.gson.Gson;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;

import java.util.ArrayList;
import java.util.Locale;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class Buy extends Activity {

    String username;
    String category_s="All",title_s="None";
    String spinner_value;
    Spinner spinner;
    final ArrayList<String>  stringArray = new ArrayList<String>();
    final ArrayList<ProductClass>  ProductArrayList = new ArrayList<ProductClass>();
    String[] array ;
    ProductClass[] productArray;
    String[] array_Queried;
    ProductClass[] product_arrayQueried;
    int count_listener=0;
    Integer[] imageId = {
            R.drawable.photo,
            R.drawable.pin,
            R.drawable.ball,
            R.drawable.bicycle,
            R.drawable.focus,
            R.drawable.laptop,
            R.drawable.book

    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_buy);
        count_listener=0;
        username= getIntent().getStringExtra("Username");
        category_s=getIntent().getStringExtra("Category");
        spinner=findViewById(R.id.spinner1);

        Log.i("Chinmaya1", "asdasdbajg");

        getProductApi();
        SearchView sv=findViewById(R.id.searchView);
        sv.setOnQueryTextListener(new SearchView.OnQueryTextListener() {
            @Override
            public boolean onQueryTextSubmit(String query) {
                title_s=query;
                if(title_s.length()==0){
                    title_s="None";
                }
               query_of_array(productArray);
                Log.i("Search_Test",title_s);
                createListView();
               return false;
            }

            @Override
            public boolean onQueryTextChange(String Text) {
                if(Text.length()==0) {
                    title_s = "None";
                }
                return false;
            }
        });


        spinner.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
                if (count_listener == 0) {
                    count_listener++;
                } else {
                    Object item = parent.getItemAtPosition(position);
                    category_s = item.toString();
                    Log.i("Spinner_Test", category_s);
                    Log.i("Product_Array", productArray[2].getTitle());
                    query_of_array(productArray);
                    createListView();
                }
            }
            @Override
            public void onNothingSelected(AdapterView<?> parent) {

            }
        });



}


public void getProductApi(){

    getApi.getList(new Callback<JsonObject>() {
        @Override
        public void onResponse(Call<JsonObject> call, Response<JsonObject> response) {

            JsonObject res = response.body();
            Log.e("Chinmaya1",res.toString());

            JsonArray jsonArray = res.getAsJsonArray("result");
            for (JsonElement jsonElement : jsonArray) {
                JsonObject product = jsonElement.getAsJsonObject();

                Log.i("Chinmaya1",product.toString());
                ProductClass productObj = new Gson().fromJson(product, ProductClass.class);
                Log.i("Chinmaya1", productObj.getTitle()+productObj.getUsername());

                stringArray.add(productObj.getTitle());
                ProductArrayList.add(productObj);
            }

            array = stringArray.toArray(new String[stringArray.size()]);
            productArray=ProductArrayList.toArray(new ProductClass[ProductArrayList.size()]);

            query_of_array(productArray);
            createListView();

        }



        @Override
        public void onFailure(Call<JsonObject> call, Throwable t) {
            Log.i(getClass().toString(),t.toString());
        }});
}
    public void createListView()
    {
        ListView listView = (ListView) findViewById(R.id.listViewReview);
        CustomList adapter = new CustomList(Buy.this, array_Queried,imageId);
        listView.setAdapter(adapter);

        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                Toast.makeText(Buy.this, "You Clicked at " + product_arrayQueried[+ position].getTitle(), Toast.LENGTH_SHORT).show();
                Intent myIntent = new Intent(Buy.this, productPage.class);
                myIntent.putExtra("Username",username);
                myIntent.putExtra("Seller_Username",product_arrayQueried[+ position].getUsername());
                myIntent.putExtra("Title",product_arrayQueried[+ position].getTitle());
                myIntent.putExtra("Description",product_arrayQueried[+ position].getDescription());
                myIntent.putExtra("Category",product_arrayQueried[+ position].getCategory());
                myIntent.putExtra("Quantity",product_arrayQueried[+ position].getQuantity());
                myIntent.putExtra("Price",product_arrayQueried[+ position].getPrice());
                startActivity(myIntent);
            }
        });


    }

    public void query_of_array(ProductClass[] productArray){
            ArrayList<ProductClass>  product_queried = new ArrayList<ProductClass>();
            ArrayList<String>  array_queried = new ArrayList<String>();

            int i;
            Log.i("Category_s",category_s);
            Log.i("Title_s",title_s);
            Log.i("sdfds","dsd");
            if(category_s.equals("All") && title_s.equals("None")) {
                Log.i("Test", "All+None");
                for (i = 0; i < productArray.length; i++) {
                    product_queried.add(productArray[i]);
                    array_queried.add(productArray[i].getTitle());
                }
            }
            else
                if (category_s.length()>0 && title_s.equals("None") && !(category_s.equals("All"))){
                    Log.i("sdfds", "Category+None");
                    int count=0;
                    for(i=0;i<productArray.length;i++){
                    if(productArray[i].getCategory().equals(category_s)){
                        count++;

                        product_queried.add(productArray[i]);
                    array_queried.add(productArray[i].getTitle());
                    }
                    }
                    Log.i("Count",String.valueOf(count));
                }
                else
                if (category_s.equals("All") && title_s.length()>0 && !(title_s.equals("None"))){
                    Log.i("sdfds", "All+Title");

                    for(i=0;i<productArray.length;i++){
                        if(productArray[i].getTitle().equals(title_s)){
                            product_queried.add(productArray[i]);
                            array_queried.add(productArray[i].getTitle());
                    }
                    }
                }
                else
                if (category_s.length()>0 && title_s.length()>0 && title_s != "None" && category_s!="All"){
                    Log.i("sdfds", "Category_s+Title");

                    for(i=0;i<productArray.length;i++){
                        if(productArray[i].getTitle().equals(title_s) && productArray[i].getCategory().equals(category_s)) {
                            product_queried.add(productArray[i]);
                            array_queried.add(productArray[i].getTitle());
                        }
                    }
                }

        product_arrayQueried=product_queried.toArray(new ProductClass[product_queried.size()]);
        array_Queried=array_queried.toArray(new String[product_queried.size()]);

        Log.i("ProductArray_Queried",String.valueOf(array_Queried.length));
        Log.i("Product_Queried",String.valueOf(product_queried.size()));
        Log.i("Product_arrayQueried",String.valueOf(product_arrayQueried.length));

    }

    }



