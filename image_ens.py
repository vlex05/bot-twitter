from PIL import Image, ImageDraw, ImageFont

def image_ens(eth_domain,tweet_text,api):
    
    W, H = (880,880)
    
    if eth_domain[-2] == '⚠':
        post_result = api.update_status(status=tweet_text)
    else:
    
        if len(eth_domain) < 18 and len(eth_domain) > 0:
            im1 = Image.open('WhaleTrackerEns/ens_fond.jpg').convert('RGB')
            draw = ImageDraw.Draw(im1)
            font = ImageFont.truetype("WhaleTrackerEns/timesNR.ttf", 104)

            w, h = draw.textsize(eth_domain,font=font,stroke_width=int(1.5))
            draw.text(((W-w)/2,531),eth_domain,(255,255,255),font=font,stroke_width=int(1.5))
            im2 = Image.open('WhaleTrackerEns/logo.png').convert('RGBA')

            newsize = (200, 200)
            im2 = im2.resize(newsize)
            Image.Image.paste(im1, im2, (int((W-200)/2), 250),mask=im2)
            im1.save('WhaleTrackerEns/final_ens.png')
            media = api.media_upload('WhaleTrackerEns/final_ens.png')
            post_result = api.update_status(status=tweet_text, media_ids=[media.media_id])

        if len(eth_domain) < 25 and len(eth_domain) > 17:
            im1 = Image.open('WhaleTrackerEns/ens_fond.jpg').convert('RGB')
            draw = ImageDraw.Draw(im1)
            font = ImageFont.truetype("WhaleTrackerEns/timesNR.ttf", 74)

            w, h = draw.textsize(eth_domain,font=font,stroke_width=int(1.5))
            draw.text(((W-w)/2,531),eth_domain,(255,255,255),font=font,stroke_width=int(1.5))
            im2 = Image.open('WhaleTrackerEns/logo.png').convert('RGBA')

            newsize = (200, 200)
            im2 = im2.resize(newsize)
            Image.Image.paste(im1, im2, (int((W-200)/2), 250),mask=im2)
            im1.save('WhaleTrackerEns/final_ens.png')
            media = api.media_upload('WhaleTrackerEns/final_ens.png')
            post_result = api.update_status(status=tweet_text, media_ids=[media.media_id])
    return(post_result)
