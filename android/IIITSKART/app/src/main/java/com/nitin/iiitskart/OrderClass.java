package com.nitin.iiitskart;

import java.util.Date;

public class OrderClass {

    String buyer;
    String sellername;
    String date;
    String product;
    String quantity;
    String total_amt;
    String price;

    OrderClass(String product,String buyer, String sellername, String quantity, String total_amt,String price){
        setBuyer(buyer);
        setSellername(sellername);
        setQuantity(quantity);
        setTotal_amt(total_amt);
        setPrice(price);
        setProduct(product);
    }

    public void setDate(String date) {
        this.date = date;
    }

    public void setPrice(String price) {
        this.price = price;
    }

    public void setBuyer(String buyer) {
        this.buyer = buyer;
    }

    public void setProduct(String product) {
        this.product = product;
    }

    public void setQuantity(String quantity) {
        this.quantity = quantity;
    }

    public void setTotal_amt(String total_amt) {
        this.total_amt = total_amt;
    }

    public void setSellername(String sellername) {
        this.sellername = sellername;
    }

    public String getBuyer() {
        return buyer;
    }

    public String getDate() {
        return date;
    }

    public String getQuantity() {
        return quantity;
    }

    public String getSellername() {
        return sellername;
    }

    public String getTotal_amt() {
        return total_amt;
    }

    public String getProduct() {
        return product;
    }

    public String getPrice() {
        return price;
    }
}
