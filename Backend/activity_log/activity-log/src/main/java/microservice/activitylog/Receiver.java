package microservice.activitylog;

import com.google.api.core.ApiFuture;
import com.google.cloud.firestore.DocumentReference;
import com.google.cloud.firestore.Firestore;
import com.google.cloud.firestore.WriteResult;
import com.google.firebase.cloud.FirestoreClient;
import com.postmarkapp.postmark.Postmark;
import com.postmarkapp.postmark.client.ApiClient;
import com.postmarkapp.postmark.client.data.model.message.Message;
import com.postmarkapp.postmark.client.data.model.message.MessageResponse;
import com.postmarkapp.postmark.client.exception.PostmarkException;

import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.stereotype.Service;

import java.io.IOException;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.HashMap;
import java.util.Map;


@Service
public class Receiver {

	ApiClient client = Postmark.getApiClient("8ec71d6b-4d86-437a-ad24-c7f332cb49a5");

	@RabbitListener(queues = {"Activity_Log"})
	public void receiveMessage(String message) throws IOException {
		DateTimeFormatter dtf = DateTimeFormatter.ofPattern("yyyy/MM/dd HH:mm:ss");
		System.out.println("Received " + message);
//		try {
//			 Json jsonObject = new JSONObject("{\"phonetype\":\"N95\",\"cat\":\"WP\"}");
//		}catch (JSONException err){
//			Log.d("Error", err.toString());
//		}
		// Firestore db = FirestoreClient.getFirestore();
		// DocumentReference docRef = db.collection("activity_log").document();
		// // Add document data using a hashmap
		// Map<String, Object> data = new HashMap<>();
		// data.put("time", dtf.format(LocalDateTime.now()));
		// data.put("message", message);
		// //asynchronously write data
		// ApiFuture<WriteResult> result = docRef.set(data);
        try {
        	Message msg = new Message("wsee.2023@scis.smu.edu.sg", "wsee.2023@scis.smu.edu.sg", "Hello from Postmark!", message);
        	MessageResponse response = client.deliverMessage(msg);
			System.out.println(response);
        } catch (Error | PostmarkException e) {
            // Handle email sending exception
            e.printStackTrace();
        }
	}
}
