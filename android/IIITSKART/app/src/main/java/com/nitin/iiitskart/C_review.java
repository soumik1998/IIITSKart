package com.nitin.iiitskart;

public class C_review {
    String rating;
    String text;
    String username;
    String seller;
    C_review(String rating,String text,String username,String seller){
        setRating(rating);
        setText(text);
        setUsername(username);
        setSeller(seller);
    }

    public void setSeller(String seller) {
        this.seller = seller;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public void setRating(String rating) {
        this.rating = rating;
    }

    public void setText(String text) {
        this.text = text;
    }


    public String getUsername() {
        return username;
    }
    public String getRating() {
        return rating;
    }

    public String getSeller() {
        return seller;
    }

    public String getText() {
        return text;
    }
}
