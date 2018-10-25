package com.nitin.iiitskart;

public class Customer {
    private String username;
    private String phone;
    private String address;
    private String blacklist;
    public Customer(String username,String phone,String address,String blacklist){
        setUsername(username);
        setAddress(address);
        setBlacklist(blacklist);
        setPhone(phone);

    }

    public void setPhone(String phone) {
        this.phone = phone;
    }

    public void setUsername(String username) {
        this.username = username;
    }



    public void setBlacklist(String blacklist) {
        this.blacklist = blacklist;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public String getUsername() {
        return username;
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

