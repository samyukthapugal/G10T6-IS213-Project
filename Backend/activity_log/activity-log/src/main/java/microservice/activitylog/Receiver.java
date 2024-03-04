package microservice.activitylog;

import com.google.api.core.ApiFuture;
import com.google.cloud.firestore.DocumentReference;
import com.google.cloud.firestore.Firestore;
import com.google.cloud.firestore.WriteResult;
import com.google.firebase.cloud.FirestoreClient;
import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.HashMap;
import java.util.Map;

@Service
public class Receiver {

	@RabbitListener(queues = {"Activity_Log"})
	public void receiveMessage(String message) {
		DateTimeFormatter dtf = DateTimeFormatter.ofPattern("yyyy/MM/dd HH:mm:ss");
		System.out.println("Received " + message);
//		try {
//			 Json jsonObject = new JSONObject("{\"phonetype\":\"N95\",\"cat\":\"WP\"}");
//		}catch (JSONException err){
//			Log.d("Error", err.toString());
//		}
		Firestore db = FirestoreClient.getFirestore();
		DocumentReference docRef = db.collection("activity_log").document();
		// Add document data using a hashmap
		Map<String, Object> data = new HashMap<>();
		data.put("time", dtf.format(LocalDateTime.now()));
		data.put("message", message);
		//asynchronously write data
		ApiFuture<WriteResult> result = docRef.set(data);
	}

}
