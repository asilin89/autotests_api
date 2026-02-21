import grpc
import user_service_pb2
import user_service_pb2_grpc
from concurrent import futures

# This is implementation of server
# Extend class UserServiceServicer from user_service_pb2_grpc module

class UserServiceServicer(user_service_pb2_grpc.UserServiceServicer):
    # context = headers in REST API
    def GetUser(self, request, context):
        print(f"Request received to GetUser method from user: {request.username}")
        return user_service_pb2_grpc.GetUserResponse(message=f"Hello, {request.username}")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_service_pb2_grpc.add_UserServiceServicer_to_server(UserServiceServicer(), server)
    server.add_insecure_port('[::]:5005')
    server.start()
    print(f"gRPC Listening on port 5005...")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()






