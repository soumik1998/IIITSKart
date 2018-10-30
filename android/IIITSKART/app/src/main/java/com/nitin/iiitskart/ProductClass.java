package com.nitin.iiitskart;

public class ProductClass {

    String title;
    int quantity;
    String description;
    Float price;
    String category;
    String username;
    String image;
    String filePath;
    ProductClass(String title,String description,String category,int quantity,float price,String username,String image,String filePath){
            setCategory(category);
            setDescription(description);
            setPrice(price);
            setQuantity(quantity);
            setTitle(title);
            setUsername(username.toLowerCase());
            setImage(image);
            setFilePath(filePath);
    }

    public void setFilePath(String filePath) {
        this.filePath = filePath;
    }

    public void setImage(String image) {
        this.image = image;
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

    public String getFilePath() {
        return filePath;
    }

    public String getUsername() {
        return username;
    }

    public String getImage() {
        return image;
    }
}
