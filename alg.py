import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
#importing numpy and matplotlib.pyplot
def func(filename):
    arr_image_0=np.genfromtxt(filename, delimiter=',',dtype='int')
    print(arr_image_0)
    shape=arr_image_0.shape
    size=arr_image_0.size
    #obtaining dimensions of imported array
    arr_identities=np.zeros(500,dtype='int')
    arr_x_coords=np.zeros(500,dtype='int')
    arr_y_coords=np.zeros(500,dtype='int')
    arr_num_pixels=np.zeros(500,dtype='int')
    arr_intensity=np.zeros(500,dtype='int')
    arr_intersecting_identities_1=np.zeros(500,dtype='int')
    #List of blocks of pixels which intersect another identities(List of the smaller identities of redundant pairs)
    arr_intersecting_identities_2=np.zeros(500,dtype='int')
    #List of blocks of pixels which intersect another identities(List of the larger identities of redundant pairs)
    arr_final_correction=np.zeros(500,dtype='int')
    #Final list of identities paired up with a particular one (redundancies)
    #initiating required arrays
    print(arr_x_coords)
    arr_stars=np.zeros((100,15),dtype='int')
    
    num_rows=shape[0]
    padding_vertical=np.zeros(num_rows,dtype=int)
    #creating a column of zeroes (1 dimensional)
    arr_image_1=np.insert(arr_image_0,0,padding_vertical,axis=1)
    #Adding the left column of padding of zeros to the image array
    print(arr_image_1)
    vertical_padding_resized=padding_vertical.reshape(-1,1)
    #resizing the 1-dimensional column to a 2-dimensional array with one column for requirements by numpy.append
    arr_image_2=np.append(arr_image_1,vertical_padding_resized,axis=1)
    #adding the right column of padding of zeros to the image array
    print(arr_image_2)
    print(arr_x_coords)
    
    shape2=arr_image_2.shape
    #obtaining dimensions of the image with added padding columns
    num_columns=shape2[1]
    padding_horizontal=np.zeros(num_columns,dtype=int)
    #creating a row of zeros(1-dimensional)
    arr_image_3=np.insert(arr_image_2,0,padding_horizontal,axis=0)
    print(arr_image_3)
    #Adding the top row of padding of zeros to the image array
    horizontal_padding_resized=padding_horizontal.reshape(1,-1)
    #resizingthe 1-dimensional row to a 2-dimensional array with one row for requirements by numpy.append
    arr_image=np.append(arr_image_3,horizontal_padding_resized,axis=0)
    #Adding the bottom row of padding to the image array
    arr_image 
    shape3=arr_image_3.shape
    size_new=arr_image.size
    num_rows_f=shape3[0]
    num_cols_f=shape3[1]
    print(arr_image)
    print(arr_x_coords)
    print(size_new)
    
    row_go=0
    col_go=0
    scatter_before_col=np.zeros(size_new,dtype='int')
    sbci=0
    scatter_before_row=np.zeros(size_new,dtype='int')
    sbri=0
    while(row_go<shape[0]):
        col_go=0
        while(col_go<shape[1]):
            if(arr_image[row_go][col_go]!=0):
                scatter_before_col[sbci]=row_go
                scatter_before_row[sbri]=col_go
                sbci+=1
                sbri+=1
            col_go+=1
        row_go+=1
    print(scatter_before_col)
    print(scatter_before_row)

    plt.figure(figsize=(10,10),dpi=100)
    plot=plt.scatter(scatter_before_col,scatter_before_row,s=0.5,color="yellow")
    plt.savefig('pic.png')
    ax=plt.axes()
    ax.set_facecolor("black")
    plt.xlabel('X',fontsize=20)
    plt.ylabel('Y',fontsize=20)
    plt.title("Stars",fontsize=50)
    
    count=0
    #'count' will keep a track of the identities of groups of pixels
    x_travel=0
    #'x_travel' will be the current row number in the matrix while travelling
    y_travel=0
    #'y_travel' will be the current column number in the matrix while travelling
    clashing_travel=0
    #'clashing_travel' will keep a track of clashings in the blocks
    #The following while loop will be for travelling across the matrix in a zig-zag pattern
    while (1):
        #The following condition is separates the cases when current element is zero and non-zero
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
                        #Here since both the previous element and the one above are non-zero, there is a redundant block.
                        #i.e. two blocks intersect. The above line gives the current element the minimum of the two values
                        arr_x_coords[(min(arr_image[x_travel-1][y_travel],arr_image[x_travel][y_travel+1]))-1]+=(x_travel)*(arr_image[x_travel][y_travel])
                        arr_y_coords[(min(arr_image[x_travel-1][y_travel],arr_image[x_travel][y_travel+1]))-1]+=(y_travel)*(arr_image[x_travel][y_travel])
                        arr_num_pixels[min(arr_image[x_travel-1][y_travel],arr_image[x_travel][y_travel+1])-1]+=1
                        arr_intensity[(min(arr_image[x_travel-1][y_travel],arr_image[x_travel][y_travel+1]))-1]+=arr_image[x_travel][y_travel]
                        arr_image[x_travel][y_travel]=min(arr_image[x_travel-1][y_travel],arr_image[x_travel][y_travel+1])
                        arr_intersecting_identities_1[clashing_travel]=min(arr_image[x_travel-1][y_travel],arr_image[x_travel][y_travel+1])
                        #This line adds the minimum of the two values to the first array of clashings, as the next element
                        arr_intersecting_identities_2[clashing_travel]=max(arr_image[x_travel-1][y_travel],arr_image[x_travel][y_travel+1])
                        #This line adds the maximum of the two values to the second array of clashings, as the next element
                        clashing_travel+=1
                        #This line increases the clashing count by 1 as we spotted a new clashing.
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
                        #Here since both the previous element and the one above are non-zero, there is a redundant block.
                        #i.e. two blocks intersect. The above line gives the current element the minimum of the two values
                        arr_x_coords[(min(arr_image[x_travel-1][y_travel],arr_image[x_travel][y_travel-1]))-1]+=(x_travel)*(arr_image[x_travel][y_travel])
                        arr_y_coords[(min(arr_image[x_travel-1][y_travel],arr_image[x_travel][y_travel-1]))-1]+=(y_travel)*(arr_image[x_travel][y_travel])
                        arr_num_pixels[(min(arr_image[x_travel-1][y_travel],arr_image[x_travel][y_travel-1]))-1]+=1
                        arr_intensity[(min(arr_image[x_travel-1][y_travel],arr_image[x_travel][y_travel-1]))-1]+=arr_image[x_travel][y_travel]
                        arr_image[x_travel][y_travel]=min(arr_image[x_travel-1][y_travel],arr_image[x_travel][y_travel-1])
                        arr_intersecting_identities_1[clashing_travel]=min(arr_image[x_travel-1][y_travel],arr_image[x_travel][y_travel-1])
                        #This line adds the minimum of the two values to the first array of clashings, as the next element
                        arr_intersecting_identities_2[clashing_travel]=max(arr_image[x_travel-1][y_travel],arr_image[x_travel][y_travel-1])
                        #This line adds the maximum of the two values to the second array of clashings, as the next element
                        clashing_travel+=1
                        #This line increases the clashing count by 1 as we spotted a new clashing.
        #The following conditions are for deciding the next element to be travelled to
        if x_travel %2==0:
            #If x_travel is even, we have to move to the left of the current element
            if x_travel==0 and y_travel==0:
                x_travel+=1
            elif y_travel==1:
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
            if y_travel+2==num_cols_f:
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
                
                
    print(arr_image)
    print(arr_x_coords)
    print(arr_identities)
    final_num_identities=0
    # final_num_identities measures final number of identities after taking care of clashings
    while(arr_identities[final_num_identities]!=0):
        final_num_identities+=1
    print(final_num_identities) 
    print(arr_y_coords)
    print(arr_intensity)
    print(arr_intersecting_identities_1)
    print(arr_intersecting_identities_2)
    print(arr_num_pixels)
    print(arr_final_correction) 
    print(clashing_travel)
    
    
    correction_travel=0
    # correction_travel will be used to travel through arr_intersecting_identities
    identity_count_1=0
    #current row number of arr_stars
    identity_count_2=0
    #current column number of arr_stars
    search=1
    # search will act as an index while searching for identities already in a row, and finding clashings in the former two arrays
    #corresponding to them

    #The following loop is used to travel through arr_intersecting_identities_1 and eliminate clashings
    while(correction_travel<arr_intersecting_identities_1.shape[0]):
        current = arr_intersecting_identities_1[correction_travel]
        # current is the current identity to be searched for
    
        #if current is -1, the element has been taken care of. If current is zero, it's not a new identity
        if(current!=-1 and current!=0):
            #if current is a valid identity, change current location in arr_stars to current
            arr_stars[identity_count_1][identity_count_2]=current
            identity_count_2+=1
            #increment column number by 1
        
        #The following loop is for searching clashings for current element and adding them all in the current row's elements    
        while(current!=0 and current!=-1):
            search1=np.array(np.where(arr_intersecting_identities_1==current))
            #The array search1 maintains the locations in arr_intersecting_identities_1 at which current is found
            search2=np.array(np.where(arr_intersecting_identities_2==current))
            #The array search2 maintains the locations in arr_intersecting_identities_2 at which current is found
            length1=search1.size
            length2=search2.size
            #length1 and length2 are sizes of search1 and search2 respectively
            search1=search1[0]
            search2=search2[0]
            #the above lines make search1 and search2 1-d Arrays instead of 2-D arrays with one row each
        
            #if any of search1 and search2 are empty, we should make the corresponding sizes 0.
            if (search1.size==0):
                length1=0
            if (search2.size==0):
                length2=0
                
            travel1=0
            travel2=0
            #travel1 will be used to travel through search1, travel2 through search2
        
            #The following loop is for travelling through search1
            while(travel1<length1):
                arr_stars[identity_count_1][identity_count_2]=arr_intersecting_identities_2[int(search1[travel1])]
                #At whichever position in arr_intersecting_identities_1 where we found current, we need to take the corresponding
                #identities from arr_intersecting_identities_2
                arr_intersecting_identities_1[search1[travel1]]=-1
                arr_intersecting_identities_2[search1[travel1]]=-1
                #changing already considered clashed identities to -1
                identity_count_2+=1
                travel1+=1
                #incrementing traversing variables
            
            #The following loop is for travelling through search2    
            while(travel2<length2):
                arr_stars[identity_count_1][identity_count_2]=arr_intersecting_identities_1[int(search2[travel2])]
                #At whichever position in arr_intersecting_identities_2 where we found current, we need to take the corresponding
                #identities from arr_intersecting_identities_1
                arr_intersecting_identities_1[search2[travel2]]=-1
                arr_intersecting_identities_2[search2[travel2]]=-1
                #changing already considered clashed identities to -1
                identity_count_2+=1
                travel2+=1
                #incrementing traversing variables
            
            current=arr_stars[identity_count_1][search]
            #changing current to next
        
            #The following loop helps break the loop if the next(and thus all next elements of current row of arr_stars) are 0
            if(current==0):
                identity_count_1+=1
                identity_count_2=0
                break
            search+=1
            #incrementing search by 1
            identity_count_1+=1
            #incrementing row number as all clashings of current star have been handled
            identity_count_2=0
            #resetting column number to 0
        correction_travel+=1
        #moving to the next position in arr_intersecting_identities_1
    print(arr_stars)
    
    row=0
    col=0
    #row and col will be used to travel through arr_stars

    #The following loop is to be used to go through arr_stars
    while(arr_stars[row][0]!=0 or row==1):
        #The following loop is to get the number of clashing identities for a single star, ie. number of non-zero elements in
        #current row of arr_stars
        while(arr_stars[row][col]!=0):
            col+=1
        elements=arr_stars[row,0:col]
        #elements takes out the non-zero
        print(elements)
        new_identity=np.min(elements)
        #The identity retained by the star would be the minimum of these identities clashing
        temp=0
        #The variable temp and the following while loop would be used to travel through elements
        while(temp<col):
            #whenever the current element is not the identity to be retained, the following loop is executed
            if(elements[temp]!=new_identity):
                arr_identities[elements[temp]-1]=0
                arr_x_coords[new_identity-1]+=arr_x_coords[elements[temp]-1]
                arr_y_coords[new_identity-1]+=arr_y_coords[elements[temp]-1]
                arr_num_pixels[new_identity-1]+=arr_num_pixels[elements[temp]-1]
                arr_intensity[new_identity-1]+=arr_intensity[elements[temp]-1]
                #We add the data from a redundant identity to the retained identity
                arr_x_coords[elements[temp]-1]=0
                arr_y_coords[elements[temp]-1]=0
                arr_num_pixels[elements[temp]-1]=0
                arr_intensity[elements[temp]-1]=0
                #Now we set the data corresponding to the redundant identity to 0
            temp+=1
            #increment travelling variable by 1
        row+=1        
        #go to next row
        
        
    print(arr_identities)
    print(arr_x_coords)
    print(arr_y_coords)
    print(arr_num_pixels)
    print(arr_intensity)
    arr_stars[:][:52]
    
    plot_x=np.zeros(final_num_identities,dtype='int')
    plot_y=np.zeros(final_num_identities,dtype='int')
    #The arrays plot_x and plot_y would maintain centroidal x and y coordinates of the stars respectively  
    s=0
    #The variable s will be used to travel through plot_x and plot_y
    while(s<final_num_identities):
        if(arr_num_pixels[s]!=0):
            plot_x[s]=int((arr_x_coords[s])/(arr_num_pixels[s]))
            plot_y[s]=int((arr_y_coords[s])/(arr_num_pixels[s]))
        else:
            plot_x[s]=0
            plot_y[s]=0
        #Setting each element to either the centroid's coordinated if star is present, or zero.       
        s+=1    
    print(plot_x)
    print(plot_y)
    
    plt.figure(figsize=(15,15),dpi=100)
    plot=plt.scatter(plot_x,plot_y,s=3,color="yellow")
    plt.savefig('pic.png')
    ax=plt.axes()
    ax.set_facecolor("black")
    plt.xlabel('X',fontsize=20)
    plt.ylabel('Y',fontsize=20)
    plt.legend(["Centroids"],fontsize=20)
    plt.title("Star centroids",fontsize=50)
    #Plots the centroids