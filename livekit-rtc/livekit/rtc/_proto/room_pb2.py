# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: room.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import e2ee_pb2 as e2ee__pb2
from . import handle_pb2 as handle__pb2
from . import participant_pb2 as participant__pb2
from . import track_pb2 as track__pb2
from . import video_frame_pb2 as video__frame__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nroom.proto\x12\rlivekit.proto\x1a\ne2ee.proto\x1a\x0chandle.proto\x1a\x11participant.proto\x1a\x0btrack.proto\x1a\x11video_frame.proto\"Y\n\x0e\x43onnectRequest\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\r\n\x05token\x18\x02 \x01(\t\x12+\n\x07options\x18\x03 \x01(\x0b\x32\x1a.livekit.proto.RoomOptions\"#\n\x0f\x43onnectResponse\x12\x10\n\x08\x61sync_id\x18\x01 \x01(\x04\"\xfd\x02\n\x0f\x43onnectCallback\x12\x10\n\x08\x61sync_id\x18\x01 \x01(\x04\x12\x12\n\x05\x65rror\x18\x02 \x01(\tH\x00\x88\x01\x01\x12&\n\x04room\x18\x03 \x01(\x0b\x32\x18.livekit.proto.OwnedRoom\x12:\n\x11local_participant\x18\x04 \x01(\x0b\x32\x1f.livekit.proto.OwnedParticipant\x12J\n\x0cparticipants\x18\x05 \x03(\x0b\x32\x34.livekit.proto.ConnectCallback.ParticipantWithTracks\x1a\x89\x01\n\x15ParticipantWithTracks\x12\x34\n\x0bparticipant\x18\x01 \x01(\x0b\x32\x1f.livekit.proto.OwnedParticipant\x12:\n\x0cpublications\x18\x02 \x03(\x0b\x32$.livekit.proto.OwnedTrackPublicationB\x08\n\x06_error\"(\n\x11\x44isconnectRequest\x12\x13\n\x0broom_handle\x18\x01 \x01(\x04\"&\n\x12\x44isconnectResponse\x12\x10\n\x08\x61sync_id\x18\x01 \x01(\x04\"&\n\x12\x44isconnectCallback\x12\x10\n\x08\x61sync_id\x18\x01 \x01(\x04\"\x82\x01\n\x13PublishTrackRequest\x12 \n\x18local_participant_handle\x18\x01 \x01(\x04\x12\x14\n\x0ctrack_handle\x18\x02 \x01(\x04\x12\x33\n\x07options\x18\x03 \x01(\x0b\x32\".livekit.proto.TrackPublishOptions\"(\n\x14PublishTrackResponse\x12\x10\n\x08\x61sync_id\x18\x01 \x01(\x04\"\x81\x01\n\x14PublishTrackCallback\x12\x10\n\x08\x61sync_id\x18\x01 \x01(\x04\x12\x12\n\x05\x65rror\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x39\n\x0bpublication\x18\x03 \x01(\x0b\x32$.livekit.proto.OwnedTrackPublicationB\x08\n\x06_error\"g\n\x15UnpublishTrackRequest\x12 \n\x18local_participant_handle\x18\x01 \x01(\x04\x12\x11\n\ttrack_sid\x18\x02 \x01(\t\x12\x19\n\x11stop_on_unpublish\x18\x03 \x01(\x08\"*\n\x16UnpublishTrackResponse\x12\x10\n\x08\x61sync_id\x18\x01 \x01(\x04\"H\n\x16UnpublishTrackCallback\x12\x10\n\x08\x61sync_id\x18\x01 \x01(\x04\x12\x12\n\x05\x65rror\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x08\n\x06_error\"\xa1\x01\n\x12PublishDataRequest\x12 \n\x18local_participant_handle\x18\x01 \x01(\x04\x12\x10\n\x08\x64\x61ta_ptr\x18\x02 \x01(\x04\x12\x10\n\x08\x64\x61ta_len\x18\x03 \x01(\x04\x12+\n\x04kind\x18\x04 \x01(\x0e\x32\x1d.livekit.proto.DataPacketKind\x12\x18\n\x10\x64\x65stination_sids\x18\x05 \x03(\t\"\'\n\x13PublishDataResponse\x12\x10\n\x08\x61sync_id\x18\x01 \x01(\x04\"E\n\x13PublishDataCallback\x12\x10\n\x08\x61sync_id\x18\x01 \x01(\x04\x12\x12\n\x05\x65rror\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\x08\n\x06_error\"P\n\x1aUpdateLocalMetadataRequest\x12 \n\x18local_participant_handle\x18\x01 \x01(\x04\x12\x10\n\x08metadata\x18\x02 \x01(\t\"/\n\x1bUpdateLocalMetadataResponse\x12\x10\n\x08\x61sync_id\x18\x01 \x01(\x04\"/\n\x1bUpdateLocalMetadataCallback\x12\x10\n\x08\x61sync_id\x18\x01 \x01(\x04\"H\n\x16UpdateLocalNameRequest\x12 \n\x18local_participant_handle\x18\x01 \x01(\x04\x12\x0c\n\x04name\x18\x02 \x01(\t\"+\n\x17UpdateLocalNameResponse\x12\x10\n\x08\x61sync_id\x18\x01 \x01(\x04\"+\n\x17UpdateLocalNameCallback\x12\x10\n\x08\x61sync_id\x18\x01 \x01(\x04\"E\n\x14SetSubscribedRequest\x12\x11\n\tsubscribe\x18\x01 \x01(\x08\x12\x1a\n\x12publication_handle\x18\x02 \x01(\x04\"\x17\n\x15SetSubscribedResponse\";\n\rVideoEncoding\x12\x13\n\x0bmax_bitrate\x18\x01 \x01(\x04\x12\x15\n\rmax_framerate\x18\x02 \x01(\x01\"$\n\rAudioEncoding\x12\x13\n\x0bmax_bitrate\x18\x01 \x01(\x04\"\x8a\x02\n\x13TrackPublishOptions\x12\x34\n\x0evideo_encoding\x18\x01 \x01(\x0b\x32\x1c.livekit.proto.VideoEncoding\x12\x34\n\x0e\x61udio_encoding\x18\x02 \x01(\x0b\x32\x1c.livekit.proto.AudioEncoding\x12.\n\x0bvideo_codec\x18\x03 \x01(\x0e\x32\x19.livekit.proto.VideoCodec\x12\x0b\n\x03\x64tx\x18\x04 \x01(\x08\x12\x0b\n\x03red\x18\x05 \x01(\x08\x12\x11\n\tsimulcast\x18\x06 \x01(\x08\x12*\n\x06source\x18\x07 \x01(\x0e\x32\x1a.livekit.proto.TrackSource\"=\n\tIceServer\x12\x0c\n\x04urls\x18\x01 \x03(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\"\x84\x02\n\tRtcConfig\x12@\n\x12ice_transport_type\x18\x01 \x01(\x0e\x32\x1f.livekit.proto.IceTransportTypeH\x00\x88\x01\x01\x12P\n\x1a\x63ontinual_gathering_policy\x18\x02 \x01(\x0e\x32\'.livekit.proto.ContinualGatheringPolicyH\x01\x88\x01\x01\x12-\n\x0bice_servers\x18\x03 \x03(\x0b\x32\x18.livekit.proto.IceServerB\x15\n\x13_ice_transport_typeB\x1d\n\x1b_continual_gathering_policy\"\xca\x01\n\x0bRoomOptions\x12\x16\n\x0e\x61uto_subscribe\x18\x01 \x01(\x08\x12\x17\n\x0f\x61\x64\x61ptive_stream\x18\x02 \x01(\x08\x12\x10\n\x08\x64ynacast\x18\x03 \x01(\x08\x12-\n\x04\x65\x32\x65\x65\x18\x04 \x01(\x0b\x32\x1a.livekit.proto.E2eeOptionsH\x00\x88\x01\x01\x12\x31\n\nrtc_config\x18\x05 \x01(\x0b\x32\x18.livekit.proto.RtcConfigH\x01\x88\x01\x01\x42\x07\n\x05_e2eeB\r\n\x0b_rtc_config\"0\n\nBufferInfo\x12\x10\n\x08\x64\x61ta_ptr\x18\x01 \x01(\x04\x12\x10\n\x08\x64\x61ta_len\x18\x02 \x01(\x04\"e\n\x0bOwnedBuffer\x12-\n\x06handle\x18\x01 \x01(\x0b\x32\x1d.livekit.proto.FfiOwnedHandle\x12\'\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x19.livekit.proto.BufferInfo\"\xf3\x0b\n\tRoomEvent\x12\x13\n\x0broom_handle\x18\x01 \x01(\x04\x12\x44\n\x15participant_connected\x18\x02 \x01(\x0b\x32#.livekit.proto.ParticipantConnectedH\x00\x12J\n\x18participant_disconnected\x18\x03 \x01(\x0b\x32&.livekit.proto.ParticipantDisconnectedH\x00\x12\x43\n\x15local_track_published\x18\x04 \x01(\x0b\x32\".livekit.proto.LocalTrackPublishedH\x00\x12G\n\x17local_track_unpublished\x18\x05 \x01(\x0b\x32$.livekit.proto.LocalTrackUnpublishedH\x00\x12\x38\n\x0ftrack_published\x18\x06 \x01(\x0b\x32\x1d.livekit.proto.TrackPublishedH\x00\x12<\n\x11track_unpublished\x18\x07 \x01(\x0b\x32\x1f.livekit.proto.TrackUnpublishedH\x00\x12:\n\x10track_subscribed\x18\x08 \x01(\x0b\x32\x1e.livekit.proto.TrackSubscribedH\x00\x12>\n\x12track_unsubscribed\x18\t \x01(\x0b\x32 .livekit.proto.TrackUnsubscribedH\x00\x12K\n\x19track_subscription_failed\x18\n \x01(\x0b\x32&.livekit.proto.TrackSubscriptionFailedH\x00\x12\x30\n\x0btrack_muted\x18\x0b \x01(\x0b\x32\x19.livekit.proto.TrackMutedH\x00\x12\x34\n\rtrack_unmuted\x18\x0c \x01(\x0b\x32\x1b.livekit.proto.TrackUnmutedH\x00\x12G\n\x17\x61\x63tive_speakers_changed\x18\r \x01(\x0b\x32$.livekit.proto.ActiveSpeakersChangedH\x00\x12\x43\n\x15room_metadata_changed\x18\x0e \x01(\x0b\x32\".livekit.proto.RoomMetadataChangedH\x00\x12Q\n\x1cparticipant_metadata_changed\x18\x0f \x01(\x0b\x32).livekit.proto.ParticipantMetadataChangedH\x00\x12I\n\x18participant_name_changed\x18\x10 \x01(\x0b\x32%.livekit.proto.ParticipantNameChangedH\x00\x12M\n\x1a\x63onnection_quality_changed\x18\x11 \x01(\x0b\x32\'.livekit.proto.ConnectionQualityChangedH\x00\x12\x34\n\rdata_received\x18\x12 \x01(\x0b\x32\x1b.livekit.proto.DataReceivedH\x00\x12I\n\x18\x63onnection_state_changed\x18\x13 \x01(\x0b\x32%.livekit.proto.ConnectionStateChangedH\x00\x12\x33\n\x0c\x64isconnected\x18\x15 \x01(\x0b\x32\x1b.livekit.proto.DisconnectedH\x00\x12\x33\n\x0creconnecting\x18\x16 \x01(\x0b\x32\x1b.livekit.proto.ReconnectingH\x00\x12\x31\n\x0breconnected\x18\x17 \x01(\x0b\x32\x1a.livekit.proto.ReconnectedH\x00\x12=\n\x12\x65\x32\x65\x65_state_changed\x18\x18 \x01(\x0b\x32\x1f.livekit.proto.E2eeStateChangedH\x00\x12%\n\x03\x65os\x18\x19 \x01(\x0b\x32\x16.livekit.proto.RoomEOSH\x00\x42\t\n\x07message\"7\n\x08RoomInfo\x12\x0b\n\x03sid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08metadata\x18\x03 \x01(\t\"a\n\tOwnedRoom\x12-\n\x06handle\x18\x01 \x01(\x0b\x32\x1d.livekit.proto.FfiOwnedHandle\x12%\n\x04info\x18\x02 \x01(\x0b\x32\x17.livekit.proto.RoomInfo\"E\n\x14ParticipantConnected\x12-\n\x04info\x18\x01 \x01(\x0b\x32\x1f.livekit.proto.OwnedParticipant\"2\n\x17ParticipantDisconnected\x12\x17\n\x0fparticipant_sid\x18\x01 \x01(\t\"(\n\x13LocalTrackPublished\x12\x11\n\ttrack_sid\x18\x01 \x01(\t\"0\n\x15LocalTrackUnpublished\x12\x17\n\x0fpublication_sid\x18\x01 \x01(\t\"d\n\x0eTrackPublished\x12\x17\n\x0fparticipant_sid\x18\x01 \x01(\t\x12\x39\n\x0bpublication\x18\x02 \x01(\x0b\x32$.livekit.proto.OwnedTrackPublication\"D\n\x10TrackUnpublished\x12\x17\n\x0fparticipant_sid\x18\x01 \x01(\t\x12\x17\n\x0fpublication_sid\x18\x02 \x01(\t\"T\n\x0fTrackSubscribed\x12\x17\n\x0fparticipant_sid\x18\x01 \x01(\t\x12(\n\x05track\x18\x02 \x01(\x0b\x32\x19.livekit.proto.OwnedTrack\"?\n\x11TrackUnsubscribed\x12\x17\n\x0fparticipant_sid\x18\x01 \x01(\t\x12\x11\n\ttrack_sid\x18\x02 \x01(\t\"T\n\x17TrackSubscriptionFailed\x12\x17\n\x0fparticipant_sid\x18\x01 \x01(\t\x12\x11\n\ttrack_sid\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\"8\n\nTrackMuted\x12\x17\n\x0fparticipant_sid\x18\x01 \x01(\t\x12\x11\n\ttrack_sid\x18\x02 \x01(\t\":\n\x0cTrackUnmuted\x12\x17\n\x0fparticipant_sid\x18\x01 \x01(\t\x12\x11\n\ttrack_sid\x18\x02 \x01(\t\"Z\n\x10\x45\x32\x65\x65StateChanged\x12\x17\n\x0fparticipant_sid\x18\x01 \x01(\t\x12-\n\x05state\x18\x02 \x01(\x0e\x32\x1e.livekit.proto.EncryptionState\"1\n\x15\x41\x63tiveSpeakersChanged\x12\x18\n\x10participant_sids\x18\x01 \x03(\t\"\'\n\x13RoomMetadataChanged\x12\x10\n\x08metadata\x18\x01 \x01(\t\"G\n\x1aParticipantMetadataChanged\x12\x17\n\x0fparticipant_sid\x18\x01 \x01(\t\x12\x10\n\x08metadata\x18\x02 \x01(\t\"?\n\x16ParticipantNameChanged\x12\x17\n\x0fparticipant_sid\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"f\n\x18\x43onnectionQualityChanged\x12\x17\n\x0fparticipant_sid\x18\x01 \x01(\t\x12\x31\n\x07quality\x18\x02 \x01(\x0e\x32 .livekit.proto.ConnectionQuality\"\x97\x01\n\x0c\x44\x61taReceived\x12(\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x1a.livekit.proto.OwnedBuffer\x12\x1c\n\x0fparticipant_sid\x18\x02 \x01(\tH\x00\x88\x01\x01\x12+\n\x04kind\x18\x03 \x01(\x0e\x32\x1d.livekit.proto.DataPacketKindB\x12\n\x10_participant_sid\"G\n\x16\x43onnectionStateChanged\x12-\n\x05state\x18\x01 \x01(\x0e\x32\x1e.livekit.proto.ConnectionState\"\x0b\n\tConnected\"\x0e\n\x0c\x44isconnected\"\x0e\n\x0cReconnecting\"\r\n\x0bReconnected\"\t\n\x07RoomEOS*P\n\x10IceTransportType\x12\x13\n\x0fTRANSPORT_RELAY\x10\x00\x12\x14\n\x10TRANSPORT_NOHOST\x10\x01\x12\x11\n\rTRANSPORT_ALL\x10\x02*C\n\x18\x43ontinualGatheringPolicy\x12\x0f\n\x0bGATHER_ONCE\x10\x00\x12\x16\n\x12GATHER_CONTINUALLY\x10\x01*N\n\x11\x43onnectionQuality\x12\x10\n\x0cQUALITY_POOR\x10\x00\x12\x10\n\x0cQUALITY_GOOD\x10\x01\x12\x15\n\x11QUALITY_EXCELLENT\x10\x02*S\n\x0f\x43onnectionState\x12\x15\n\x11\x43ONN_DISCONNECTED\x10\x00\x12\x12\n\x0e\x43ONN_CONNECTED\x10\x01\x12\x15\n\x11\x43ONN_RECONNECTING\x10\x02*3\n\x0e\x44\x61taPacketKind\x12\x0e\n\nKIND_LOSSY\x10\x00\x12\x11\n\rKIND_RELIABLE\x10\x01\x42\x10\xaa\x02\rLiveKit.Protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'room_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\rLiveKit.Proto'
  _globals['_ICETRANSPORTTYPE']._serialized_start=6186
  _globals['_ICETRANSPORTTYPE']._serialized_end=6266
  _globals['_CONTINUALGATHERINGPOLICY']._serialized_start=6268
  _globals['_CONTINUALGATHERINGPOLICY']._serialized_end=6335
  _globals['_CONNECTIONQUALITY']._serialized_start=6337
  _globals['_CONNECTIONQUALITY']._serialized_end=6415
  _globals['_CONNECTIONSTATE']._serialized_start=6417
  _globals['_CONNECTIONSTATE']._serialized_end=6500
  _globals['_DATAPACKETKIND']._serialized_start=6502
  _globals['_DATAPACKETKIND']._serialized_end=6553
  _globals['_CONNECTREQUEST']._serialized_start=106
  _globals['_CONNECTREQUEST']._serialized_end=195
  _globals['_CONNECTRESPONSE']._serialized_start=197
  _globals['_CONNECTRESPONSE']._serialized_end=232
  _globals['_CONNECTCALLBACK']._serialized_start=235
  _globals['_CONNECTCALLBACK']._serialized_end=616
  _globals['_CONNECTCALLBACK_PARTICIPANTWITHTRACKS']._serialized_start=469
  _globals['_CONNECTCALLBACK_PARTICIPANTWITHTRACKS']._serialized_end=606
  _globals['_DISCONNECTREQUEST']._serialized_start=618
  _globals['_DISCONNECTREQUEST']._serialized_end=658
  _globals['_DISCONNECTRESPONSE']._serialized_start=660
  _globals['_DISCONNECTRESPONSE']._serialized_end=698
  _globals['_DISCONNECTCALLBACK']._serialized_start=700
  _globals['_DISCONNECTCALLBACK']._serialized_end=738
  _globals['_PUBLISHTRACKREQUEST']._serialized_start=741
  _globals['_PUBLISHTRACKREQUEST']._serialized_end=871
  _globals['_PUBLISHTRACKRESPONSE']._serialized_start=873
  _globals['_PUBLISHTRACKRESPONSE']._serialized_end=913
  _globals['_PUBLISHTRACKCALLBACK']._serialized_start=916
  _globals['_PUBLISHTRACKCALLBACK']._serialized_end=1045
  _globals['_UNPUBLISHTRACKREQUEST']._serialized_start=1047
  _globals['_UNPUBLISHTRACKREQUEST']._serialized_end=1150
  _globals['_UNPUBLISHTRACKRESPONSE']._serialized_start=1152
  _globals['_UNPUBLISHTRACKRESPONSE']._serialized_end=1194
  _globals['_UNPUBLISHTRACKCALLBACK']._serialized_start=1196
  _globals['_UNPUBLISHTRACKCALLBACK']._serialized_end=1268
  _globals['_PUBLISHDATAREQUEST']._serialized_start=1271
  _globals['_PUBLISHDATAREQUEST']._serialized_end=1432
  _globals['_PUBLISHDATARESPONSE']._serialized_start=1434
  _globals['_PUBLISHDATARESPONSE']._serialized_end=1473
  _globals['_PUBLISHDATACALLBACK']._serialized_start=1475
  _globals['_PUBLISHDATACALLBACK']._serialized_end=1544
  _globals['_UPDATELOCALMETADATAREQUEST']._serialized_start=1546
  _globals['_UPDATELOCALMETADATAREQUEST']._serialized_end=1626
  _globals['_UPDATELOCALMETADATARESPONSE']._serialized_start=1628
  _globals['_UPDATELOCALMETADATARESPONSE']._serialized_end=1675
  _globals['_UPDATELOCALMETADATACALLBACK']._serialized_start=1677
  _globals['_UPDATELOCALMETADATACALLBACK']._serialized_end=1724
  _globals['_UPDATELOCALNAMEREQUEST']._serialized_start=1726
  _globals['_UPDATELOCALNAMEREQUEST']._serialized_end=1798
  _globals['_UPDATELOCALNAMERESPONSE']._serialized_start=1800
  _globals['_UPDATELOCALNAMERESPONSE']._serialized_end=1843
  _globals['_UPDATELOCALNAMECALLBACK']._serialized_start=1845
  _globals['_UPDATELOCALNAMECALLBACK']._serialized_end=1888
  _globals['_SETSUBSCRIBEDREQUEST']._serialized_start=1890
  _globals['_SETSUBSCRIBEDREQUEST']._serialized_end=1959
  _globals['_SETSUBSCRIBEDRESPONSE']._serialized_start=1961
  _globals['_SETSUBSCRIBEDRESPONSE']._serialized_end=1984
  _globals['_VIDEOENCODING']._serialized_start=1986
  _globals['_VIDEOENCODING']._serialized_end=2045
  _globals['_AUDIOENCODING']._serialized_start=2047
  _globals['_AUDIOENCODING']._serialized_end=2083
  _globals['_TRACKPUBLISHOPTIONS']._serialized_start=2086
  _globals['_TRACKPUBLISHOPTIONS']._serialized_end=2352
  _globals['_ICESERVER']._serialized_start=2354
  _globals['_ICESERVER']._serialized_end=2415
  _globals['_RTCCONFIG']._serialized_start=2418
  _globals['_RTCCONFIG']._serialized_end=2678
  _globals['_ROOMOPTIONS']._serialized_start=2681
  _globals['_ROOMOPTIONS']._serialized_end=2883
  _globals['_BUFFERINFO']._serialized_start=2885
  _globals['_BUFFERINFO']._serialized_end=2933
  _globals['_OWNEDBUFFER']._serialized_start=2935
  _globals['_OWNEDBUFFER']._serialized_end=3036
  _globals['_ROOMEVENT']._serialized_start=3039
  _globals['_ROOMEVENT']._serialized_end=4562
  _globals['_ROOMINFO']._serialized_start=4564
  _globals['_ROOMINFO']._serialized_end=4619
  _globals['_OWNEDROOM']._serialized_start=4621
  _globals['_OWNEDROOM']._serialized_end=4718
  _globals['_PARTICIPANTCONNECTED']._serialized_start=4720
  _globals['_PARTICIPANTCONNECTED']._serialized_end=4789
  _globals['_PARTICIPANTDISCONNECTED']._serialized_start=4791
  _globals['_PARTICIPANTDISCONNECTED']._serialized_end=4841
  _globals['_LOCALTRACKPUBLISHED']._serialized_start=4843
  _globals['_LOCALTRACKPUBLISHED']._serialized_end=4883
  _globals['_LOCALTRACKUNPUBLISHED']._serialized_start=4885
  _globals['_LOCALTRACKUNPUBLISHED']._serialized_end=4933
  _globals['_TRACKPUBLISHED']._serialized_start=4935
  _globals['_TRACKPUBLISHED']._serialized_end=5035
  _globals['_TRACKUNPUBLISHED']._serialized_start=5037
  _globals['_TRACKUNPUBLISHED']._serialized_end=5105
  _globals['_TRACKSUBSCRIBED']._serialized_start=5107
  _globals['_TRACKSUBSCRIBED']._serialized_end=5191
  _globals['_TRACKUNSUBSCRIBED']._serialized_start=5193
  _globals['_TRACKUNSUBSCRIBED']._serialized_end=5256
  _globals['_TRACKSUBSCRIPTIONFAILED']._serialized_start=5258
  _globals['_TRACKSUBSCRIPTIONFAILED']._serialized_end=5342
  _globals['_TRACKMUTED']._serialized_start=5344
  _globals['_TRACKMUTED']._serialized_end=5400
  _globals['_TRACKUNMUTED']._serialized_start=5402
  _globals['_TRACKUNMUTED']._serialized_end=5460
  _globals['_E2EESTATECHANGED']._serialized_start=5462
  _globals['_E2EESTATECHANGED']._serialized_end=5552
  _globals['_ACTIVESPEAKERSCHANGED']._serialized_start=5554
  _globals['_ACTIVESPEAKERSCHANGED']._serialized_end=5603
  _globals['_ROOMMETADATACHANGED']._serialized_start=5605
  _globals['_ROOMMETADATACHANGED']._serialized_end=5644
  _globals['_PARTICIPANTMETADATACHANGED']._serialized_start=5646
  _globals['_PARTICIPANTMETADATACHANGED']._serialized_end=5717
  _globals['_PARTICIPANTNAMECHANGED']._serialized_start=5719
  _globals['_PARTICIPANTNAMECHANGED']._serialized_end=5782
  _globals['_CONNECTIONQUALITYCHANGED']._serialized_start=5784
  _globals['_CONNECTIONQUALITYCHANGED']._serialized_end=5886
  _globals['_DATARECEIVED']._serialized_start=5889
  _globals['_DATARECEIVED']._serialized_end=6040
  _globals['_CONNECTIONSTATECHANGED']._serialized_start=6042
  _globals['_CONNECTIONSTATECHANGED']._serialized_end=6113
  _globals['_CONNECTED']._serialized_start=6115
  _globals['_CONNECTED']._serialized_end=6126
  _globals['_DISCONNECTED']._serialized_start=6128
  _globals['_DISCONNECTED']._serialized_end=6142
  _globals['_RECONNECTING']._serialized_start=6144
  _globals['_RECONNECTING']._serialized_end=6158
  _globals['_RECONNECTED']._serialized_start=6160
  _globals['_RECONNECTED']._serialized_end=6173
  _globals['_ROOMEOS']._serialized_start=6175
  _globals['_ROOMEOS']._serialized_end=6184
# @@protoc_insertion_point(module_scope)