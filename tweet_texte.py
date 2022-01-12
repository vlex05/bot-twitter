def tweet_texte(eth_price, last_eth_domain,eth_domain,usd_price,actual_owner,before_owner,json_url):
    
    if eth_price >= 10:
        tweet_text = ('🚨🚨 '+ eth_domain[0].upper()+eth_domain[1:]+' bought for '+str(eth_price)+' ETH ($'+str(usd_price)+' USD) by '+actual_owner+' from '+before_owner+'. '+json_url['assets'][0]['permalink']+' #ensdomains '+ '#ethereum')
    
    elif eth_price >= 5:   
        tweet_text = ('❗❗ '+ eth_domain[0].upper()+eth_domain[1:]+' bought for '+str(eth_price)+' ETH ($'+str(usd_price)+' USD) by '+actual_owner+' from '+before_owner+'. '+json_url['assets'][0]['permalink']+' #ensdomains '+ '#ethereum')
    
    else:     
        tweet_text = (eth_domain[0].upper()+eth_domain[1:]+' bought for '+str(eth_price)+' ETH ($'+str(usd_price)+' USD) by '+actual_owner+' from '+before_owner+'. '+json_url['assets'][0]['permalink']+' #ensdomains '+ '#ethereum')

    if eth_price > last_eth_domain['bigest_sale'][0]: 
        tweet_text = '🚨🚨🚨🚨 NEW RECORD 🚨🚨🚨🚨 ' + eth_domain[0].upper()+eth_domain[1:]+' bought for '+str(eth_price)+' ETH ($'+str(usd_price)+' USD) by '+actual_owner+' from '+before_owner+'. '+json_url['assets'][0]['permalink']+' #ensdomains '+ '#ethereum'
        last_eth_domain['bigest_sale'][0] = eth_price
        last_eth_domain.to_csv('WhaleTrackerEns/last_ens_name.csv')
    return(tweet_text)
