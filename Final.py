import numpy as np
import matplotlib.pyplot as plt
#importing numpy and matplotlib.pyplot
file=open('Test_image.txt')
rows=file.read().split()
for counter in range(0,len(rows)):
    rows[counter]=rows[counter].split(',')
Arr_image_0=np.array(rows,dtype=int)    
Arr_image_0
#importing the given image in an array form from the appropriate file
print(Arr_image_0)
shape=Arr_image_0.shape
#obtaining dimensions of imported array
Arr_identities=np.zeros(shape)
Arr_x_coords=np.zeros(shape)
Arr_y_coords=np.zeros(shape)
Arr_num_pixels=np.zeros(shape)
Arr_intensity_values=np.zeros(shape)
Arr_intersecting_identities_1=np.zeros(shape)
Arr_intersecting_identities_2=np.zeros(shape)
Arr_final_correction=np.zeros(shape)
#initiating required arrays
Num_rows=shape[0]
padding_vertical=np.zeros(Num_rows,dtype=int)
#creating a column of zeroes (1 dimensional)
Arr_image_1=np.insert(Arr_image_0,0,padding_vertical,axis=1)
#Adding the left column of padding of zeros to the image array
print(Arr_image_1)
vertical_padding_resized=padding_vertical.reshape(-1,1)
#resizing the 1-dimensional column to a 2-dimensional array with one column for requirements by numpy.append
Arr_image_2=np.append(Arr_image_1,vertical_padding_resized,axis=1)
#adding the right column of padding of zeros to the image array
print(Arr_image_2)
shape2=Arr_image_2.shape
#obtaining dimensions of the image with added padding columns
Num_columns=shape2[1]
padding_horizontal=np.zeros(Num_columns,dtype=int)
#creating a row of zeros(1-dimensional)
Arr_image_3=np.insert(Arr_image_2,0,padding_horizontal,axis=0)
print(Arr_image_3)
#Adding the top row of padding of zeros to the image array
horizontal_padding_resized=padding_horizontal.reshape(1,-1)
#resizingthe 1-dimensional row to a 2-dimensional array with one row for requirements by numpy.append
Arr_image=np.append(Arr_image_3,horizontal_padding_resized,axis=0)
#Adding the bottom row of padding to the image array
Arr_image


count=0
#'count' will keep a track of the identities of groups of pixels
x_travel=0
#'x_travel' will be the current row number in the matrix while travelling
y_travel=0
#'y_travel' will be the current column number in the matrix while travelling
redundancy_travel=0
#'redundancy_travel' will keep a track of redundancies in the blocks
#The following while loop will be for travelling across the matrix in a zig-zag pattern
while (0==0):
    #The following condition is separaates the cases when current element is zero and non-zero
    if arr_image[x_travel][y_travel] !=0:
        #If x_travel is even, we have to move to the left of the current element
        if x_travel %2 ==0:
            #Here, the previous element travelled from is that having the coordinates x_travel, y_travel +1
            #The following condition separates the cases when the previous element is zero and non-zero
            if arr_image[x_travel][y_travel+1] ==0:
                #The following condition separates the cases when the element above current element is zero and non-zero
                if arr_image[x_travel-1][y_travel]==0:
                    arr_x_coords[count]+=(x_travel)*(arr_image[x_travel][y_travel])
                    arr_y_coords[count]+=(y_travel)*(arr_image[x_travel][y_travel])
                    arr_num_pixels[count]+=1
                    arr_intensity[count]+=arr_image[x_travel][y_travel]
                    #The above lines add corresponding information of the element to the respective arrays
                    arr_identities[count]=count+1
                    #As here, both the previous element and the element above are zero, we found a new identity.
                    #Hence, the above line adds a new identity to the identities' array
                    arr_image[x_travel][y_travel]=(count+1)
                    #This line changes the current element's value to its identity
                    count+=1
                    #As we found a new identity, we increase the count by 1.
                else:
                    arr_x_coords[(arr_image[x_travel-1][y_travel])-1]+=(x_travel)*(arr_image[x_travel][y_travel])
                    arr_y_coords[(arr_image[x_travel-1][y_travel])-1]+=(y_travel)*(arr_image[x_travel][y_travel])
                    arr_num_pixels[(arr_image[x_travel-1][y_travel])-1]+=1
                    arr_intensity[(arr_image[x_travel-1][y_travel])-1]+=arr_image[x_travel][y_travel]
                    #The above lines add corresponding information of the element to the respective arrays
                    arr_image[x_travel][y_travel]=arr_image[x_travel-1][y_travel]
                    #As the element above the current isn't zero, the current element takes its value.
            else:
                if arr_image[x_travel-1][y_travel] == 0 or arr_image[x_travel-1][y_travel] == arr_image[x_travel][y_travel+1]:
                    arr_x_coords[(arr_image[x_travel][y_travel+1])-1]+=(x_travel)*(arr_image[x_travel][y_travel])
                    arr_y_coords[(arr_image[x_travel][y_travel+1])-1]+=(y_travel)*(arr_image[x_travel][y_travel])
                    arr_num_pixels[(arr_image[x_travel][y_travel+1])-1]+=1
                    arr_intensity[(arr_image[x_travel][y_travel+1])-1]+=arr_image[x_travel][y_travel]
                    #The above lines add corresponding information of the element to the respective arrays
                    arr_image[x_travel][y_travel]=arr_image[x_travel][y_travel+1]
                    #As the previous element is non-zero, the current element takes its value.
                else:
                    arr_image[x-travel][y-travel]=min(arr_image[x_travel-1][y_travel],arr_image[x_travel][y_travel+1])
                    #Here since both the previous element and the one above are non-zero, there is a redundant block.
                    #i.e. two blocks intersect. The above line gives the current element the minimum of the two values
                    arr_intersecting_identities_1[redundancy_travel]=min(arr_image[x_travel-1][y_travel],arr_image[x_travel][y_travel+1])
                    #This line adds the minimum of the two values to the first array of redundancies, as the next element
                    arr_intersecting_identities_2[redundancy_travel]=max(arr_image[x_travel-1][y_travel],arr_image[x_travel][y_travel+1])
                    #This line adds the maximum of the two values to the second array of redundancies, as the next element
                    redundancy_travel+=1
                    #This line increases the redundancy count by 1 as we spotted a new redundancy.
        #If x_travel is odd, we have to move to the right of the current element            
        else:
            #Here, the previous element travelled from is that having the coordinates x_travel, y_travel -1
            #The following condition separates the cases when the previous element is zero and non-zero
            if arr_image[x_travel][y_travel-1] ==0:
                #The following condition separates the cases when the element above current element is zero and non-zero
                if arr_image[x_travel-1][y_travel]==0:
                    arr_x_coords[count]+=((x_travel)*(arr_image[x_travel][y_travel]))
                    arr_y_coords[count]+=((y_travel)*(arr_image[x_travel][y_travel]))
                    arr_num_pixels[count]+=1
                    arr_intensity[count]+=(arr_image[x_travel][y_travel])
                    #The above lines add corresponding information of the element to the respective arrays
                    arr_identities[count]=(count+1)
                    #As here, both the previous element and the element above are zero, we found a new identity.
                    #Hence, the above line adds a new identity to the identities' array
                    arr_image[x_travel][y_travel]=(count+1)
                    #This line changes the current element's value to its identity
                    count+=1
                    #As we found a new identity, we increase the count by 1.
                else:
                    arr_x_coords[(arr_image[x_travel-1][y_travel])-1]+=(x_travel)*(arr_image[x_travel][y_travel])
                    arr_y_coords[(arr_image[x_travel-1][y_travel])-1]+=(y_travel)*(arr_image[x_travel][y_travel])
                    arr_num_pixels[(arr_image[x_travel-1][y_travel])-1]+=1
                    arr_intensity[(arr_image[x_travel-1][y_travel])-1]+=arr_image[x_travel][y_travel]
                    #The above lines add corresponding information of the element to the respective arrays
                    arr_image[x_travel][y_travel]=arr_image[x_travel-1][y_travel]
                    #As the element above the current isn't zero, the current element takes its value.
            else:
                if arr_image[x_travel-1][y_travel] == 0 or arr_image[x_travel-1][y_travel] == arr_image[x_travel][y_travel-1]:
                    arr_x_coords[(arr_image[x_travel][y_travel-1])-1]+=(x_travel)*(arr_image[x_travel][y_travel])
                    arr_y_coords[(arr_image[x_travel][y_travel-1])-1]+=(y_travel)*(arr_image[x_travel][y_travel])
                    arr_num_pixels[(arr_image[x_travel][y_travel-1])-1]+=1
                    arr_intensity[(arr_image[x_travel][y_travel-1])-1]+=arr_image[x_travel][y_travel]
                    #The above lines add corresponding information of the element to the respective arrays
                    arr_image[x_travel][y_travel]=arr_image[x_travel][y_travel-1]
                    #As the previous element is non-zero, the current element takes its value.
                else:
                    arr_image[x-travel][y-travel]=min(arr_image[x_travel-1][y_travel],arr_image[x_travel][y_travel-1])
                    #Here since both the previous element and the one above are non-zero, there is a redundant block.
                    #i.e. two blocks intersect. The above line gives the current element the minimum of the two values
                    arr_intersecting_identities_1[redundancy_travel]=min(arr_image[x_travel-1][y_travel],arr_image[x_travel][y_travel-1])
                    #This line adds the minimum of the two values to the first array of redundancies, as the next element
                    arr_intersecting_identities_2[redundancy_travel]=max(arr_image[x_travel-1][y_travel],arr_image[x_travel][y_travel-1])
                    #This line adds the maximum of the two values to the second array of redundancies, as the next element
                    redundancy_travel+=1
                    #This line increases the redundancy count by 1 as we spotted a new redundancy.
    #The following conditions are for deciding the next element to be travelled to                
    if x_travel %2==0:
        #If x_travel is even, we have to move to the left of the current element
        if y_travel==0:
            #But if we can't travel left anymore, we have to travel to the next row.
            if x_travel+1==num_rows_f:
                #But if there is no row next, the image has been traversed fully. Thus we exit the while loop
                break
            else:
                #If next row exists, increase the row number
                x_travel+=1
        else:
            #If we aren't at the extreme left , decrease the column number
            y_travel-=1
    else:
        #If x_travel is odd, we have to move to the right of the current element
        if y_travel+1==num_cols_f:
            #But if we can't travel right anymore, we have to travel to the next row.
            if x_travel+1==num_rows_f:
                #But if there is no row next, the image has been traversed fully. Thus we exit the while loop.
                break
            else:
                #If next row exists, we increase row number by 1.
                x_travel+=1
        else:
            #If we aren't at the extreme right, we increase the column number by 1.
            y_travel+=1
            
correction_travel=0
identity_count_1=0
identity_count_2=0
search=1
while(correction_travel<arr_intersecting_identities_1.shape[0]):
    current = arr_intersecting_identities_1[correction_travel]
    #if(current!=0):
        #print(current)
        #print("Current^")
        #print(identity_count_1)
        #print(identity_count_2)
    if(current!=-1 and current!=0):
        arr_stars[identity_count_1][identity_count_2]=current
        identity_count_2+=1
    while(current!=0 and current!=-1):
        search1=np.array(np.where(arr_intersecting_identities_1==current))
        search2=np.array(np.where(arr_intersecting_identities_2==current))
        length1=search1.size
        length2=search2.size
        search1=search1[0]
        search2=search2[0]
        #print(current)
        #print(arr_intersecting_identities_1)
        #print(arr_intersecting_identities_2)
        #print(search1)
        #print(search2)
        if (search1.size==0):
            length1=0
        #    print("done1")
        if (search2.size==0):
            length2=0
         #   print("done2")
        travel1=0
        travel2=0
        #print(length1)
        #print(length2)        
        while(travel1<length1):
            arr_stars[identity_count_1][identity_count_2]=arr_intersecting_identities_2[int(search1[travel1])]
            arr_intersecting_identities_1[search1[travel1]]=-1
            arr_intersecting_identities_2[search1[travel1]]=-1
            identity_count_2+=1
            travel1+=1
        while(travel2<length2):
            arr_stars[identity_count_1][identity_count_2]=arr_intersecting_identities_1[int(search2[travel2])]
            arr_intersecting_identities_1[search2[travel2]]=-1
            arr_intersecting_identities_2[search2[travel2]]=-1
            identity_count_2+=1
            travel2+=1            
        current=arr_stars[identity_count_1][search]
        if(current==0):
            break
        search+=1
        identity_count_1+=1
        identity_count_2=0
    correction_travel+=1
print(arr_stars)    
    
row=0
col=0
while(arr_stars[row][0]!=0):
    while(arr_stars[row][col]!=0):
        col+=1
    elements=arr_stars[row,0:col]
    new_identity=np.min(elements)
    temp=0
    while(temp<col):
        if(elements[temp]!=new_identity):
            arr_identities[elements[temp]-1]=0
            arr_x_coords[new_identity-1]+=arr_x_coords[elements[temp]-1]
            arr_y_coords[new_identity-1]+=arr_y_coords[elements[temp]-1]
            arr_num_pixels[new_identity-1]+=arr_num_pixels[elements[temp]-1]
            arr_intensity[new_identity-1]+=arr_intensity[elements[temp]-1]
            arr_x_coords[elements[temp]-1]=0
            arr_y_coords[elements[temp]-1]=0
            arr_num_pixels[elements[temp]-1]=0
            arr_intensity[elements[temp]-1]=0
        temp+=1
    row+=1            
            
            

            