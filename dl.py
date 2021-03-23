import sys, os
from skillshare import Skillshare, splash


# or by class ID:
# dl.download_course_by_class_id(189505397)

def main():
    ck = """
   device_session_id=9026eaff-e2a5-4b5c-940a-d28a384f6304; show-like-copy=1; visitor_tracking=utm_campaign%3D%26utm_source%3D%28direct%29%26utm_medium%3D%28none%29%26utm_term%3D%26referrer%3D%26referring_username%3D; first_landing=utm_campaign%3D%26utm_source%3D%28direct%29%26utm_medium%3D%28none%29%26utm_term%3D%26referrer%3D%26referring_username%3D; _gcl_au=1.1.1859151710.1614912981; __pdst=4c8c7545e3004f9ba11131172ff09fb9; IR_gbd=skillshare.com; sm_uuid=1614913584047; _scid=373bd65d-46a2-40fc-8e34-54f8be9d2ac4; __stripe_mid=c528dc02-9da2-4628-9585-be81a5b794d606ac1d; _pin_unauth=dWlkPU1EWmtZbUU1WWprdE5qSmtOUzAwTkRCaUxUazBNR1l0T0RZeVpqTmtNamc1TUROaQ; __qca=P0-447870354-1614912984158; G_ENABLED_IDPS=google; __ssid=13d3d52f5d3cc900310729834ec77f5; _ga=GA1.2.1191895916.1615001704; ss_hide_site_banner=1615167562.498; CAPTIONS=off; dismiss_transcripts_tooltip=1; g_state={"i_p":1615333355998,"i_l":2}; __utma=99704988.1191895916.1615001704.1615500708.1615500708.1; __utmc=99704988; __utmz=99704988.1615500708.1.1.utmcsr=paypal.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=99704988.|1=visitor-type=user=1; YII_CSRF_TOKEN=VUlMdEk4ejg4NTRUcVFPcmdkcVkzZ1BZODlrWEtTajE1rVEA7FjI-4lAHmQsVd5b16RCISxsxg7A8VgMsQ15NA%3D%3D; _sctr=1|1616108400000; PHPSESSID=593e2d8935f42a56cf505f0e9931a1ec; IR_4650=1616209599952%7C0%7C1616209597969%7C%7C; IR_PI=97b626f7-14e7-11eb-8af2-42010a246e2e%7C1616295999952; _derived_epik=dj0yJnU9elZQQlYyNnU1Tl9hSTFDcExxWGVSSi1sQURhWXNKZDkmbj1zTGhBSDdJLWxmUTBseUhObGhpMi1RJm09NyZ0PUFBQUFBR0JWWnNBJnJtPWUmcnQ9QUFBQUFHQlVySFU; _uetsid=2eb34df087ff11eb8df2f9acba627d4a; _uetvid=60c92be06bc211eb80ff6744a4bcee95; __stripe_sid=6d51de04-73e0-43e1-ad64-8db3157ee1cf41947e
    """
    dl = Skillshare("skillshare_user_=")
    course_url = sys.argv[1]
    dl.download_course_by_url(course_url)


if __name__ == "__main__":
    splash()
    main()
