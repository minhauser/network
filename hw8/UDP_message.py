import struct

# UDP 헤더 필드 값 설정
source_port = 12345      # 예시 송신자 포트 번호
destination_port = 80     # 예시 수신자 포트 번호
length = 8                # UDP 헤더의 길이 (데이터 없음)
checksum = 0              # 체크섬 (계산하지 않음)

# '!'는 네트워크 바이트 오더(Big-endian)를 의미하고,
# 'H'는 2바이트(16비트) unsigned short를 의미합니다.
udp_header_format = '!HHHH'

# UDP 헤더 패킹
packed_header = struct.pack(
    udp_header_format,
    source_port,
    destination_port,
    length,
    checksum)
print(f"Packed UDP Header: {packed_header.hex()}")

# UDP 헤더 언패킹
unpacked_header = struct.unpack(udp_header_format, packed_header)
print(f"Unpacked UDP Header: Source Port={unpacked_header[0]}, "
      f"Destination Port={unpacked_header[1]}, "
      f"Length={unpacked_header[2]}, "
      f"Checksum={unpacked_header[3]}")
