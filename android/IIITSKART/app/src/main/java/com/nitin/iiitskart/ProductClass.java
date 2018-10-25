package com.nitin.iiitskart;

public class ProductClass {

    String title;
    int quantity;
    String description;
    Float price;
    String category;
    String username;
    ProductClass(String title,String description,String category,int quantity,float price,String username){
            setCategory(category);
            setDescription(description);
            setPrice(price);
            setQuantity(quantity);
            setTitle(title);
            setUsername(username.toLowerCase());
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    public void setPrice(Float price) {
        this.price = price;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public Float getPrice() {
        return price;
    }

    public int getQuantity() {
        return quantity;
    }

    public String getCategory() {
        return category;
    }

    public String getDescription() {
        return description;
    }

    public String getTitle() {
        return title;
    }

    public String getUsername() {
        return username;
    }
}
