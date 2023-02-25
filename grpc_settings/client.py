import grpc_config_pb2
import grpc_config_pb2_grpc
import grpc


def get_user(email):
    # print("In run")
    with grpc.insecure_channel('localhost:1694') as channel:
        stub = grpc_config_pb2_grpc.UserStub(channel)
        user_info_request = grpc_config_pb2.UserInforequest(email=email)
        user_info_reply = stub.UserInfo(user_info_request)
        print("SayHello Response Received:")
        print(user_info_reply)
        return user_info_reply.id


# if __name__ == "__main__":
#     run()