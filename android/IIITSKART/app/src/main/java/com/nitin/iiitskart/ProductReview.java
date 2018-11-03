package com.nitin.iiitskart;

public class ProductReview {
    String sellerusername;
    String rating;
    String text;
    String title;

    ProductReview(String rating,String text,String title,String sellerusername){
        setRating(rating);
        setSellerusername(sellerusername);
        setText(text);
        setTitle(title);
    }

    public void setText(String text) {
        this.text = text;
    }

    public void setRating(String rating) {
        this.rating = rating;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public void setSellerusername(String sellerusername) {
        this.sellerusername = sellerusername;
    }

    public String getText() {
        return text;
    }

    public String getRating() {
        return rating;
    }

    public String getTitle() {
        return title;
    }

    public String getSellerusername() {
        return sellerusername;
    }
}
