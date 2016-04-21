import numpy
import string
import zlib
import base64
import numpy as np
import copy


class Payload:
    def __init__(self, img=None, compressionLevel = -1, xml= None):

        self.img = img
        self.xml = xml
        self.compression_level = compressionLevel

        #raising value and type error below this
        if (img is None and xml is None):
            raise ValueError('ckuabvca')

        elif (compressionLevel < -1 or compressionLevel > 9):
            raise ValueError

        #write code here for type error if either img or xml contains incorrect types

        elif(type(img) is not numpy.ndarray and img is not None):
            raise TypeError('dsads')

        elif(type(xml) is not str and xml is not None):
            raise TypeError('Dasdaf')

        elif (img is not None):
            xml_value = self.make_xml()
            self.xml = xml_value

        elif (xml is not None):
            image_returned_xml = self.reconstruct_image()
            self.img = image_returned_xml

        #raising value and type error above this


        #print(self.img)

    def reconstruct_image(self):
        xml_file_net = self.xml.split()
        payload_type_image_temp1 = xml_file_net[4].split('"')

        payload_type_image = payload_type_image_temp1[1]

        compressed_temp = xml_file_net[6].split('"')

        compressed_image = compressed_temp[1]


        size_temp = xml_file_net[5].split('"')
        size_x_temp = size_temp[1].split(',')


        size_x = int(size_x_temp[0])
        size_y = int(size_x_temp[1])
        #size_y_temp = size_x_temp

        decoded_value = base64.b64decode(xml_file_net[7])

        if(compressed_image == 'True'):
            decompressed_value = zlib.decompress(decoded_value)
        else:
            decompressed_value = decoded_value

        decompressed_value = list(decompressed_value)

        length_divide_3 = int(len(decompressed_value) / 3)

        red_list = []
        blue_list = []
        green_list = []
        final_list = []
        counter = 0
        if(payload_type_image == 'Gray'):
            gray_image = np.resize(decompressed_value, (size_x,size_y))
            return gray_image

        elif(payload_type_image == 'Color'):


            red_list = decompressed_value[ 0 : length_divide_3 ]
            green_list = decompressed_value[length_divide_3 : 2 * length_divide_3]
            blue_list = decompressed_value[2 * length_divide_3 : 3 * length_divide_3]
            counter = 0
            for i in range(len(red_list)):
                final_list.append(red_list[i])
                final_list.append(green_list[i])
                final_list.append(blue_list[i])

            color_image = np.resize(final_list, (size_x,size_y, 3))
            return color_image


    def make_xml(self):

        red_list = []
        green_list = []
        blue_list = []
        final_list = []
        counter = 0


        if(type(self.img[0][0]) is numpy.ndarray):
            payload_type = 'Color'
            for list1 in self.img:
                for list2 in list1:
                    for val in list2:
                            if counter % 3 == 0:
                                red_list.append(val)
                            elif counter % 3 == 1:
                                green_list.append(val)
                            else:
                                blue_list.append(val)
                            counter += 1
            x_value = len(self.img)
            y_value = len(self.img[0])

        else:
            payload_type = 'Gray'
            for list1 in self.img:
                for list2 in list1:
                    final_list.append(list2)
            x_value = len(self.img)
            y_value = len(self.img[0])



        for value in red_list:
            final_list.append(value)

        for value in green_list:
            final_list.append(value)

        for value in blue_list:
            final_list.append(value)


        final_nd_array = numpy.asarray(final_list)

        if(self.compression_level is not -1):
            compressed_value = zlib.compress(final_nd_array, self.compression_level)
            compressed_value_encoded = str(base64.b64encode(compressed_value), encoding='UTF-8')
            compressed = 'True'
        else:
            compressed_value_encoded = str(base64.b64encode(final_nd_array), encoding='UTF-8')
            compressed = 'False'



        size = "{0},{1}".format(x_value,y_value)
        xml_str_value = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<payload type=\"{0}\" size=\"{1}\" compressed=\"{2}\">\n{3}\n</payload>".format(payload_type, size, compressed, compressed_value_encoded)

        return xml_str_value

        #image to list


#<?xm[88 chars]e">\neAEA+/8EABYVFxYWFhgYGRcZGBoaGxocGxwgHx4eI[921715 chars]oad>
#<?xm[88 chars]e">\nb\'eAEA+/8EABYVFxYWFhgYGRcZGBoaGxocGxwgHx[921720 chars]oad>

class Carrier:
    def __init__(self,img):
        self.img = img
        if(type(self.img) is not numpy.ndarray or self.img is None):
            raise TypeError

    def clean(self):
        new_image = copy.deepcopy(self.img)
        list = []
        if(type(new_image[0][0]) is numpy.ndarray):
            for list1 in new_image:
                for list2 in list1:
                    counter = 0
                    for value in list2:
                        if(value % 2 != 0):
                            list2[counter] = list2[counter] - 1
                        counter = counter + 1

        else:
            for list1 in new_image:
                index = 0
                for value in list1:
                    if(value % 2 != 0):
                        list1[index] = list1[index] - 1
                    index = index + 1



        return new_image


    def payloadExists(self):

        if(type(self.img[0][0]) is numpy.ndarray):
            counter = 0
            red_list = []
            check_list = []
            for list1 in self.img:
                if(len(red_list) == 8):
                    break
                for list2 in list1:
                    if(len(red_list) == 8):
                        break
                    for val in list2:
                            if counter % 3 == 0:
                                red_list.append(val)
                            counter+=1

                            if(len(red_list) == 8):
                                break

            for value in red_list:
                if(len(check_list) != 8):

                    if(value % 2 == 0):
                        check_list.append(0)
                    else:
                        check_list.append(1)

            s = "".join(map(str, check_list))
            ascii_value = int(s, base=2)

            if(ascii_value == 60):
                return True

            else:
                return False

        else:
            check_list_gray = []
            counter = 0
            for list1 in self.img:
                for val in list1:
                    if(val % 2 == 0):
                        check_list_gray.append(0)
                        counter = counter + 1
                    else:
                        check_list_gray.append(1)
                        counter = counter + 1

                    if(counter == 8):
                        s = "".join(map(str, check_list_gray))
                        ascii_value = int(s, base=2)

                        if(ascii_value == 60):
                            return True

                        else:
                            return False

    def extractPayload(self):
        if(self.payloadExists() == False):
            raise Exception


        red_list = []
        green_list = []
        blue_list = []
        counter = 0
        final_list = []
        payload_list = []
        payload_string = ""


        if(type(self.img[0][0]) is numpy.ndarray):
            payload_type = 'Color'
            for list1 in self.img:
                for list2 in list1:
                    for val in list2:
                            if counter % 3 == 0:
                                red_list.append(val)
                            elif counter % 3 == 1:
                                green_list.append(val)
                            else:
                                blue_list.append(val)
                            counter += 1

            counter = 0
            ten_ctr = 0
            payload_list = []
            final1_list = red_list + green_list + blue_list
            new_string = ""

            for value in final1_list:
                if(value % 2 == 0):
                    payload_list.append(0)
                    counter = counter + 1
                else:
                    payload_list.append(1)
                    counter = counter + 1

                if(counter == 8):
                    s = "".join(map(str, payload_list))
                    ascii_value = int(s, base=2)
                    counter = 0
                    payload_string += chr(ascii_value)
                    payload_list = []
                    ten_ctr = ten_ctr + 1

                    if(ten_ctr % 10 == 0):

                        if('</payload>' in payload_string):
                            return_object = Payload(xml= payload_string)
                            return return_object

        else:
            check_list_gray = []
            counter = 0
            ten_ctr = 0
            for list1 in self.img:
                for val in list1:
                    if(val % 2 == 0):
                        check_list_gray.append(0)
                        counter = counter + 1
                    else:
                        check_list_gray.append(1)
                        counter = counter + 1

                    if(counter == 8):
                        s = "".join(map(str, check_list_gray))
                        ascii_value = int(s, base=2)
                        counter = 0
                        payload_string += chr(ascii_value)
                        check_list_gray = []
                        ten_ctr = ten_ctr + 1

                        if(ten_ctr % 10 == 0):
                            if('</payload>' in payload_string):
                                return_object = Payload(xml= payload_string)
                                return return_object




        return None




    def embedPayload(self, payload, override = False):
        if(type(payload) is not Payload):
            raise TypeError

        if(override == False and self.payloadExists() == True):
            raise Exception


        if(type(self.img[0][0]) is numpy.ndarray):
            if(3 * len(self.img) * len(self.img[0]) < len(payload.xml) * 8):
                raise ValueError

        else:
            if(len(self.img) * len(self.img[0]) < len(payload.xml) * 8):
                raise ValueError

        list_binary_encode = []
        for character in payload.xml:
            ascii_value = ord(character)
            binary_value = '{0:08b}'.format(ascii_value)
            for i in binary_value:
                list_binary_encode.append(int(i))

        temp_img = copy.deepcopy(self.img)

        counter = 0
        red_list = []
        green_list = []
        blue_list = []
        final_list =[]
        length_divide_3 = 0

        if(type(self.img[0][0]) is numpy.ndarray):
            payload_type = 'Color'
            size_x = len(self.img)
            size_y = len(self.img[0])
            for list1 in self.img:
                for list2 in list1:
                    for val in list2:
                            if counter % 3 == 0:
                                red_list.append(val)
                            elif counter % 3 == 1:
                                green_list.append(val)
                            else:
                                blue_list.append(val)
                            counter += 1

            final_list = red_list + green_list + blue_list
            counter = 0
            length_divide_3 = int(len(final_list) / 3)

            for value in final_list:
                if(counter + 1 > len(list_binary_encode)):
                    break

                if(value % 2 == 0) and (list_binary_encode[counter] == 0):
                    counter = counter  + 1

                elif(value % 2 == 1) and (list_binary_encode[counter] == 0):
                    final_list[counter] = final_list[counter] - 1
                    counter = counter + 1

                elif(value % 2 == 1) and (list_binary_encode[counter] == 1):
                    counter = counter  + 1

                elif(value % 2 == 0) and (list_binary_encode[counter] == 1):
                    final_list[counter] = final_list[counter] + 1
                    counter = counter + 1

            red_list = final_list[ 0 : length_divide_3 ]
            green_list = final_list[length_divide_3 : 2 * length_divide_3]
            blue_list = final_list[2 * length_divide_3 : 3 * length_divide_3]

            final_list = []
            for i in range(len(red_list)):
                final_list.append(red_list[i])
                final_list.append(green_list[i])
                final_list.append(blue_list[i])

            color_image = np.resize(final_list, (size_x,size_y, 3))

            return color_image




        else:
            for list1 in temp_img:
                index = 0
                if(counter + 1 > len(list_binary_encode)):
                    break
                for value in list1:
                    if(counter + 1 > len(list_binary_encode)):
                        break

                    if(value % 2 == 0) and (list_binary_encode[counter] == 0):
                        index = index + 1
                        counter = counter  + 1

                    elif(value % 2 == 1) and (list_binary_encode[counter] == 0):
                        list1[index] = list1[index] - 1
                        index = index + 1
                        counter = counter + 1

                    elif(value % 2 == 1) and (list_binary_encode[counter] == 1):
                        index = index + 1
                        counter = counter  + 1

                    elif(value % 2 == 0) and (list_binary_encode[counter] == 1):
                        list1[index] = list1[index] + 1
                        index = index + 1
                        counter = counter + 1
        return temp_img


if __name__ == "__main__":
    pass
