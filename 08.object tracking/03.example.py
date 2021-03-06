import cv2
import sys

# 동영상 열기
cap = cv2.VideoCapture('../cv2/video/passenger_01.mp4')

if not cap.isOpened():
    print('Video open failed!')
    sys.exit()

# 트래커 객체 생성

# Kernelized Correlation Filters
# KCF가 그나마 빠른 알고리즘
#tracker = cv2.TrackerKCF_create()

# Minimum Output Sum of Squared Error
# 빠르게 동작하는 편
#tracker = cv2.TrackerMOSSE_create()

# Discriminative Correlation Filter with Channel and Spatial Reliability
# 앞의 두 가지 방법보다 강인하게 추적을 함. 그대신 느림
tracker = cv2.TrackerCSRT_create()
M
# GOTURN은 딥러닝 기반. 실행하려면 딥러닝 관련 파일을 다운받아서 가중치 파일을 저장해야지 동작 가능

# 첫 번째 프레임에서 추적 ROI 설정
ret, frame = cap.read()

if not ret:
    print('Frame read failed!')
    sys.exit()

# frame 이라는 이름으로 부분영상 추출
rc = cv2.selectROI('frame', frame)
# 초깃값 설정
tracker.init(frame, rc)

# 매 프레임 처리
while True:
    ret, frame = cap.read()

    if not ret:
        print('Frame read failed!')
        sys.exit()

    # 추척 $ ROI 사각형 업데이트
    # 매 프래임마다 update하고 rc값 받아옴
    ret, rc = tracker.update(frame)
    
    # floate 형태로 rc값을 받으므로 int로 변환해서 list로 감싸고 tuple로 변환
    rc = tuple([int(_) for _ in rc])
    cv2.rectangle(frame, rc, (0, 0, 255), 2)
    
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) == 27:
        break

cv2.destroyAllWindows()
