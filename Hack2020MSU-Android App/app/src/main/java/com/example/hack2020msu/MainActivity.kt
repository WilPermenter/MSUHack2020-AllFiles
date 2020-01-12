package com.example.hack2020msu

import android.content.ActivityNotFoundException
import android.content.Intent
import android.net.Uri
import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.example.hack2020msu.R.layout.activity_main


class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        val button0 = findViewById<Button>(R.id.btn0)
        val button1 = findViewById<Button>(R.id.btn1)
        val button2 = findViewById<Button>(R.id.btn2)

        findViewById<TextView>(R.id.textView0)

        button0.setOnClickListener {
            sendEmail("0")
        }
        button1.setOnClickListener {
            sendEmail("1")
        }
        button2.setOnClickListener {
            sendEmail("2")
        }


    }

    private fun sendEmail(value: String) {


        val to = "bullyhack2020@gmail.com"
        val emailIntent = Intent(Intent.ACTION_SEND)
        emailIntent.setDataAndType(Uri.parse("mailto:"),"text/plain")
        emailIntent.putExtra(Intent.EXTRA_EMAIL, "bullyhack2020@gmail.com")
        emailIntent.putExtra(Intent.EXTRA_SUBJECT, "Empty")
        emailIntent.putExtra(Intent.EXTRA_TEXT, value)
        emailIntent.type = ("message/rfc822")
        try {
            startActivity(Intent.createChooser(emailIntent, "Send mail..."))
            finish()
            //Log.i("Finished sending email...", "")
        } catch (ex: ActivityNotFoundException) {
            Toast.makeText(
                this@MainActivity,
                "There is no email client installed.",
                Toast.LENGTH_SHORT
            ).show()
        }

    }
}

