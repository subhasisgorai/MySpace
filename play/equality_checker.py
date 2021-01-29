def check_equality(samples, item1, item2):
    if samples and len(samples) > 0 and item1 and item2 :
        if item1 in samples and item1 == item2:
            return True
        clouds = __process_samples(samples)
        return item2 in clouds[item1]

    
def __process_samples(samples):
    clouds = None
    for item in samples:
        if not clouds:
            clouds = dict()
        tokens = item.split('=')
        if tokens and len(tokens) == 2:
            a, b = tokens
            cloud_a = clouds[a] if a in clouds else None
            cloud_b = clouds[b] if b in clouds else None
            
            if not cloud_a and not cloud_b:
                cloud = {a, b}
                clouds[a] = clouds[b] = cloud
            elif not cloud_a or not cloud_b:
                cloud = cloud_a if cloud_a else cloud_b
                __add_to_cloud_and_assign(clouds, cloud, a)
                __add_to_cloud_and_assign(clouds, cloud, b)
            else:
                cloud = cloud_a | cloud_b
                clouds[a] = clouds[b] = cloud
    return clouds            

            
def __add_to_cloud_and_assign(clouds, cloud, item):
    if cloud:
        cloud.add(item)
        clouds[item] = cloud

        
if __name__ == '__main__':
    print check_equality(['a=b', 'b=c', 'c=d', 'd=e', 'b=z', 'k=m'], 'a', 'k')          
    print check_equality(['a=b', 'b=c', 'c=d', 'd=e', 'b=z', 'k=m'], 'a', 'z')          
