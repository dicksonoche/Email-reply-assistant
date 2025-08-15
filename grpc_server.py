import grpc
from concurrent import futures
import logging
import protobuf.email_pb2 as email_pb2
import protobuf.email_pb2_grpc as email_pb2_grpc
from app.retrieval import retrieve_similar
from app.generation import generate_reply

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class EmailServicer(email_pb2_grpc.EmailServiceServicer):
    def DraftReply(self, request, context):
        try:
            logger.info(f"gRPC received query: {request.text[:50]}...")
            contexts = retrieve_similar(request.text)
            reply = generate_reply(request.text, contexts)
            return email_pb2.ReplyResponse(reply=reply)
        except Exception as e:
            logger.error(f"gRPC error: {str(e)}")
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return email_pb2.ReplyResponse()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    email_pb2_grpc.add_EmailServiceServicer_to_server(EmailServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    logger.info("gRPC server running on port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()