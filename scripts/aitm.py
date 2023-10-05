import struct

from mitmproxy import tcp

# mitm[proxy|dump] runs this for every raw TCP packet it receives.
def tcp_message(flow: tcp.TCPFlow):
    # most recent message
    latest = flow.messages[-1]

    # is this a request or a response?
    req = latest.from_client
    # message body (use bytearray so we can modify it)
    msg = bytearray(latest.content)

    # make sure there's enough data to unpack the Modbus ADU/PDU
    if len(msg) > 8:
        tid, pid, length, uid, fc = struct.unpack(">HHHBB", msg[:8])
        # ADU is always 7; last bit is length of rest of packet, including
        # itself, so we end up subtracting one from the length to get end of
        # packet.
        end = 7 + length - 1

        # start at 8 since we grabbed function code above
        data = msg[8:end]

        print(f'TID: {tid}')
        print(f'PID: {pid}')
        print(f'LEN: {length}')
        print(f'UID: {uid}')
        print(f'FC:  {fc}')
        print(f'DAT: {data}')

        if not req:
            # read input register, so we know what response should look like;
            # count of values, then actual values (2 bits each).
            if fc == 4:
                count = int(msg[8])

                start = 9
                end   = start + count

                while start < end:
                    value, = struct.unpack(">H", msg[start:start+2])
                    print(f'VALUE: {int(value)}')

                    start += 2 # each value is 2 bits each

                # replace values with 0
                msg[9:end] = bytearray(b'\x00' * count)
                flow.messages[-1].content = msg
