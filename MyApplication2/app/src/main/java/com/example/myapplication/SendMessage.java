package com.example.myapplication;

import android.os.AsyncTask;

import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.Socket;

public class SendMessage extends AsyncTask<String, Void, Void> {

    private Exception exception;
    @Override
    protected Void doInBackground(String... characs)
    {
        try{
            try{

                Socket ss = new Socket("192.168.1.8", 8888);


                PrintWriter outToServer = new PrintWriter(
                        new OutputStreamWriter(
                                ss.getOutputStream()));
                outToServer.print(characs[0]);
                outToServer.flush();

            } catch(IOException e1)
            {
                e1.printStackTrace();
            }
        } catch(Exception e1)
        {
            this.exception = e1;
        }
        return null;
    }
}