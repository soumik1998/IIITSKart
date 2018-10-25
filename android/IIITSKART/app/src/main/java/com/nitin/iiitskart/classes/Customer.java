package com.nitin.iiitskart.classes;

public class Customer {
    private String user;
    private String phone;
    private String address;
    private String blacklist;
    public Customer(String user,String phone,String address,String blacklist){

        setAddress(address);
        setBlacklist(blacklist);
        setPhone(phone);
        setUser(user);
    }

    public void setUser(String user) {
        this.user = user;
    }

    public String getUser() {
        return user;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }

    public void setBlacklist(String blacklist) {
        this.blacklist = blacklist;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public String getPhone() {
        return phone;
    }


    public String getBlacklist() {
        return blacklist;
    }

    public String getAddress() {
        return address;
    }

}

