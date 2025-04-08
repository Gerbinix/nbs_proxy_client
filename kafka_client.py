from kafka import KafkaProducer
import json


def produce_message(producer, topic, message):
    try:
        # Invia il messaggio e attende l'acknowledgment
        future = producer.send(topic, message)
        record_metadata = future.get(timeout=10)
        print(
            f"Messaggio inviato con successo al topic {record_metadata.topic} (partition {record_metadata.partition}, offset {record_metadata.offset})")
    except Exception as e:
        print("Errore durante l'invio del messaggio:", e)


if __name__ == "__main__":
    # Configura il producer per connettersi al broker Kafka esposto tramite Nginx Proxy Manager
    producer = KafkaProducer(
        bootstrap_servers=['188.34.141.13:39092'],
        value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Serializza il messaggio in JSON
    )

    topic = "nbs_request"
    # Definisci il messaggio da inviare (qui come esempio, puoi modificarlo a tuo piacimento)
    message = {"id": 1, "content": "Questo è un messaggio di prova inviato a nbs_request."}

    # Invia il messaggio al topic
    produce_message(producer, topic, message)

    # Assicura che tutti i messaggi siano stati inviati e chiudi il producer
    producer.flush()
    producer.close()
