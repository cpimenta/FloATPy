"""
Module for computing second deriatives with finite differencing.
"""

import numpy

def computeSecondOrderSecondDerivative(data, dx, direction = 0, component_idx = 0, uses_one_sided = True):
    """
    Computing second derivative using explicit second order finite differencing.
    """
    
    data_shape = data.shape
    
    # Check whether the direction is valid.
    
    if direction < 0 or direction > 2:
        raise RuntimeError('Direction < 0 or > 2 is invalid!')
    
    # Check whether the dimension of data is valid.
    
    if data.ndim < 2:
        raise RuntimeError('Shape of data is invalid!')
    
    # Check whether the component_idx is valid.
    
    if component_idx >= data_shape[0] or component_idx < 0:
        raise RuntimeError('Component index is invalid!')
    
    # Check whether data size is large enough for second order second derivative.
    
    if uses_one_sided == True:
        if direction == 0:
            if data_shape[1] < 4:
                raise RuntimeError('First dimension of data is not large enough!')
        
        elif direction == 1:
            if data_shape[2] < 4:
                raise RuntimeError('Second dimension of data is not large enough!')
        
        elif direction == 2:
            if data_shape[3] < 4:
                raise RuntimeError('Third dimension of data is not large enough!')
    
    else:
        if direction == 0:
            if data_shape[1] < 3:
                raise RuntimeError('First dimension of data is not large enough!')

        elif direction == 1:
            if data_shape[2] < 3:
                raise RuntimeError('Second dimension of data is not large enough!')

        elif direction == 2:
            if data_shape[3] < 3:
                raise RuntimeError('Third dimension of data is not large enough!')
    
    # Initialize container to store the derivatives. The elements in the container
    # are initialized as NAN values.
    data_shape = numpy.delete(data_shape, [0])
    diff_data = numpy.empty(data_shape)
    diff_data[:] = numpy.NAN
    
    # Compute the derivatives in the interior of the domain.
    
    if direction == 0:
        if diff_data.ndim == 1:
            diff_data[1:-1] = (data[component_idx, 0:-2] - 2.0*data[component_idx, 1:-1] \
                               + data[component_idx, 2:])/(dx*dx)
        
        elif diff_data.ndim == 2:
            diff_data[1:-1, :] = (data[component_idx, 0:-2, :] - 2.0*data[component_idx, 1:-1, :] \
                                  + data[component_idx, 2:, :])/(dx*dx)
        
        elif diff_data.ndim == 3:
            diff_data[1:-1, :, :] = (data[component_idx, 0:-2, :, :] - 2.0*data[component_idx, 1:-1, :, :] \
                                  + data[component_idx, 2:, :, :])/(dx*dx)
        
        else:
            raise RuntimeError('Data dimension > 3 not supported!')
    
    elif direction == 1:
        if diff_data.ndim < 2:
            raise IOError('There is no second direction in data with less than two dimensions!')
        
        elif diff_data.ndim == 2:
            diff_data[:, 1:-1] = (data[component_idx, :, 0:-2] - 2.0*data[component_idx, :, 1:-1] \
                                  + data[component_idx, :, 2:])/(dx*dx)
        
        elif diff_data.ndim == 3:
            diff_data[:, 1:-1, :] = (data[component_idx, :, 0:-2, :] - 2.0*data[component_idx, :, 1:-1, :] \
                                     + data[component_idx, :, 2:, :])/(dx*dx)
        
        else:
            raise RuntimeError('Data dimension > 3 not supported!')
    
    elif direction == 2:
        if diff_data.ndim < 3:
            raise IOError('There is no third direction in data with less than three dimensions!')
        
        elif diff_data.ndim == 3:
            diff_data[:, :, 1:-1] = (data[component_idx, :, :, 0:-2] - 2.0*data[component_idx, :, :, 1:-1] \
                                     + data[component_idx, :, :, 2:])/(dx*dx)
        
        else:
            raise RuntimeError('Data dimension > 3 not supported!')
    
    # Compute the derivatives at the boundaries.
    
    if uses_one_sided == True:
        if direction == 0:
            if diff_data.ndim == 1:
                diff_data[0] = (2.0*data[component_idx, 0] - 5.0*data[component_idx, 1] \
                                + 4.0*data[component_idx, 2] - data[component_idx, 3])/(dx*dx)
                
                diff_data[-1] = (-data[component_idx, -4] + 4.0*data[component_idx, -3] \
                                 - 5.0*data[component_idx, -2] + 2.0*data[component_idx, -1])/(dx*dx)
            
            elif diff_data.ndim == 2:
                diff_data[0, :] = (2.0*data[component_idx, 0, :] - 5.0*data[component_idx, 1, :] \
                                   + 4.0*data[component_idx, 2, :] - data[component_idx, 3, :])/(dx*dx)
                
                diff_data[-1, :] = (-data[component_idx, -4, :] + 4.0*data[component_idx, -3, :] \
                                    - 5.0*data[component_idx, -2, :] + 2.0*data[component_idx, -1, :])/(dx*dx)

            
            elif diff_data.ndim == 3:
                diff_data[0, :, :] = (2.0*data[component_idx, 0, :, :] - 5.0*data[component_idx, 1, :, :] \
                                      + 4.0*data[component_idx, 2, :, :] - data[component_idx, 3, :, :])/(dx*dx)
                
                diff_data[-1, :, :] = (-data[component_idx, -4, :, :] + 4.0*data[component_idx, -3, :, :] \
                                       - 5.0*data[component_idx, -2, :, :] + 2.0*data[component_idx, -1, :, :])/(dx*dx)
            
            else:
                raise RuntimeError('Data dimension > 3 not supported!')
    
    elif direction == 1:
            if diff_data.ndim < 2:
                raise RuntimeError('There is no second direction in data with less than two dimensions!')
            
            elif diff_data.ndim == 2:
                diff_data[:, 0] = (2.0*data[component_idx, :, 0] - 5.0*data[component_idx, :, 1] \
                                   + 4.0*data[component_idx, :, 2] - data[component_idx, :, 3])/(dx*dx)
                
                diff_data[:, -1] = (-data[component_idx, :, -4] + 4.0*data[component_idx, :, -3] \
                                    - 5.0*data[component_idx, :, -2] + 2.0*data[component_idx, :, -1])/(dx*dx)
            
            elif diff_data.ndim == 3:
                diff_data[:, 0, :] = (2.0*data[component_idx, :, 0, :] - 5.0*data[component_idx, :, 1, :] \
                                   + 4.0*data[component_idx, :, 2, :] - data[component_idx, :, 3, :])/(dx*dx)
                
                diff_data[:, -1, :] = (-data[component_idx, :, -4, :] + 4.0*data[component_idx, :, -3, :] \
                                    - 5.0*data[component_idx, :, -2, :] + 2.0*data[component_idx, :, -1, :])/(dx*dx)
            
            else:
                raise RuntimeError('Data dimension > 3 not supported!')
    
    elif direction == 2:
            if diff_data.ndim < 3:
                raise IOError('There is no third direction in data with less than three dimensions!')
            
            elif diff_data.ndim == 3:
                diff_data[:, :, 0] = (2.0*data[component_idx, :, :, 0] - 5.0*data[component_idx, :, :, 1] \
                                      + 4.0*data[component_idx, :, :, 2] - data[component_idx, :, :, 3])/(dx*dx)
                
                diff_data[:, :, -1] = (-data[component_idx, :, :, -4] + 4.0*data[component_idx, :, :, -3] \
                                       - 5.0*data[component_idx, :, :, -2] + 2.0*data[component_idx, :, :, -1])/(dx*dx)
            
            else:
                raise RuntimeError('Data dimension > 3 not supported!')
    
    return diff_data


def computeFourthOrderSecondDerivative(data, dx, direction = 0, component_idx = 0, uses_one_sided = True):
    """
    Computing second derivative using explicit fourth order finite differencing.
    """
    
    data_shape = data.shape
    
    # Check whether the direction is valid.
    
    if direction < 0 or direction > 2:
        raise RuntimeError('Direction < 0 or > 2 is invalid!')
    
    # Check whether the dimension of data is valid.
    
    if data.ndim < 2:
        raise RuntimeError('Shape of data is invalid!')
    
    # Check whether the component_idx is valid.
    
    if component_idx >= data_shape[0] or component_idx < 0:
        raise RuntimeError('Component index is invalid!')
    
    # Check whether data size is large enough for fourth order second derivative.
    
    if uses_one_sided == True:
        if direction == 0:
            if data_shape[1] < 6:
                raise RuntimeError('First dimension of data is not large enough!')
        
        elif direction == 1:
            if data_shape[2] < 6:
                raise RuntimeError('Second dimension of data is not large enough!')
        
        elif direction == 2:
            if data_shape[3] < 6:
                raise RuntimeError('Third dimension of data is not large enough!')
    
    else:
        if direction == 0:
            if data_shape[1] < 5:
                raise RuntimeError('First dimension of data is not large enough!')
        
        elif direction == 1:
            if data_shape[2] < 5:
                raise RuntimeError('Second dimension of data is not large enough!')
        
        elif direction == 2:
            if data_shape[3] < 5:
                raise RuntimeError('Third dimension of data is not large enough!')
    
    # Initialize container to store the derivatives. The elements in the container
    # are initialized as NAN values.
    data_shape = numpy.delete(data_shape, [0])
    diff_data = numpy.empty(data_shape)
    diff_data[:] = numpy.NAN
    
    # Compute the derivatives in the interior of the domain.
    
    if direction == 0:
        if diff_data.ndim == 1:
            diff_data[2:-2] = (-1.0/12.0*data[component_idx, 0:-4] + 4.0/3.0*data[component_idx, 1:-3] \
                               - 5.0/2.0*data[component_idx, 2:-2] + 4.0/3.0*data[component_idx, 3:-1] \
                               - 1.0/12.0*data[component_idx, 4:])/(dx*dx)
        
        elif diff_data.ndim == 2:
            diff_data[2:-2, :] = (-1.0/12.0*data[component_idx, 0:-4, :] + 4.0/3.0*data[component_idx, 1:-3, :] \
                                  - 5.0/2.0*data[component_idx, 2:-2, :] + 4.0/3.0*data[component_idx, 3:-1, :] \
                                  - 1.0/12.0*data[component_idx, 4:, :])/(dx*dx)
        
        elif diff_data.ndim == 3:
            diff_data[2:-2, :, :] = (-1.0/12.0*data[component_idx, 0:-4, :, :] + 4.0/3.0*data[component_idx, 1:-3, :, :] \
                                     - 5.0/2.0*data[component_idx, 2:-2, :, :] + 4.0/3.0*data[component_idx, 3:-1, :, :] \
                                     - 1.0/12.0*data[component_idx, 4:, :, :])/(dx*dx)
        
        else:
            raise RuntimeError('Data dimension > 3 not supported!')
    
    elif direction == 1:
        if diff_data.ndim < 2:
            raise IOError('There is no second direction in data with less than two dimensions!')
        
        elif diff_data.ndim == 2:
            diff_data[:, 2:-2] = (-1.0/12.0*data[component_idx, :, 0:-4] + 4.0/3.0*data[component_idx, :, 1:-3] \
                                  - 5.0/2.0*data[component_idx, :, 2:-2] + 4.0/3.0*data[component_idx, :, 3:-1] \
                                  - 1.0/12.0*data[component_idx, :, 4:])/(dx*dx)
        
        elif diff_data.ndim == 3:
            diff_data[:, 2:-2, :] = (-1.0/12.0*data[component_idx, :, 0:-4, :] + 4.0/3.0*data[component_idx, :, 1:-3, :] \
                                     - 5.0/2.0*data[component_idx, :, 2:-2, :] + 4.0/3.0*data[component_idx, :, 3:-1, :] \
                                     - 1.0/12.0*data[component_idx, :, 4:, :])/(dx*dx)
        
        else:
            raise RuntimeError('Data dimension > 3 not supported!')
    
    elif direction == 2:
        if diff_data.ndim < 3:
            raise IOError('There is no third direction in data with less than three dimensions!')
        
        elif diff_data.ndim == 3:
            diff_data[:, :, 2:-2] = (-1.0/12.0*data[component_idx, :, :, 0:-4] + 4.0/3.0*data[component_idx, :, :, 1:-3] \
                                     - 5.0/2.0*data[component_idx, :, :, 2:-2] + 4.0/3.0*data[component_idx, :, :, 3:-1] \
                                     - 1.0/12.0*data[component_idx, :, :, 4:])/(dx*dx)
        
        else:
            raise RuntimeError('Data dimension > 3 not supported!')
    
    # Compute the derivatives at the boundaries.
    
    if uses_one_sided == True:
        if direction == 0:
            if diff_data.ndim == 1:
                diff_data[0] = (15.0/4.0*data[component_idx, 0] - 77.0/6.0*data[component_idx, 1] \
                                + 107.0/6.0*data[component_idx, 2] - 13.0*data[component_idx, 3] \
                                + 61.0/12.0*data[component_idx, 4] - 5.0/6.0*data[component_idx, 5])/(dx*dx)
                
                diff_data[1] = (5.0/6.0*data[component_idx, 0] - 5.0/4.0*data[component_idx, 1] \
                                - 1.0/3.0*data[component_idx, 2] + 7.0/6.0*data[component_idx, 3] \
                                - 1.0/2.0*data[component_idx, 4] + 1.0/12.0*data[component_idx, 5])/(dx*dx)
                
                diff_data[-2] = (1.0/12.0*data[component_idx, -6] - 1.0/2.0*data[component_idx, -5] \
                                 + 7.0/6.0*data[component_idx, -4] - 1.0/3.0*data[component_idx, -3] \
                                 - 5.0/4.0*data[component_idx, -2] + 5.0/6.0*data[component_idx, -1])/(dx*dx)
                
                diff_data[-1] = (-5.0/6.0*data[component_idx, -6] + 61.0/12.0*data[component_idx, -5] \
                                 - 13.0*data[component_idx, -4] + 107.0/6.0*data[component_idx, -3] \
                                 - 77.0/6.0*data[component_idx, -2] + 15.0/4.0*data[component_idx, -1])/(dx*dx)
            
            elif diff_data.ndim == 2:
                diff_data[0, :] = (15.0/4.0*data[component_idx, 0, :] - 77.0/6.0*data[component_idx, 1, :] \
                                   + 107.0/6.0*data[component_idx, 2, :] - 13.0*data[component_idx, 3, :] \
                                   + 61.0/12.0*data[component_idx, 4, :] - 5.0/6.0*data[component_idx, 5, :])/(dx*dx)
                
                diff_data[1, :] = (5.0/6.0*data[component_idx, 0, :] - 5.0/4.0*data[component_idx, 1, :] \
                                   - 1.0/3.0*data[component_idx, 2, :] + 7.0/6.0*data[component_idx, 3, :] \
                                   - 1.0/2.0*data[component_idx, 4, :] + 1.0/12.0*data[component_idx, 5, :])/(dx*dx)
                
                diff_data[-2, :] = (1.0/12.0*data[component_idx, -6, :] - 1.0/2.0*data[component_idx, -5, :] \
                                    + 7.0/6.0*data[component_idx, -4, :] - 1.0/3.0*data[component_idx, -3, :] \
                                    - 5.0/4.0*data[component_idx, -2, :] + 5.0/6.0*data[component_idx, -1, :])/(dx*dx)
                
                diff_data[-1, :] = (-5.0/6.0*data[component_idx, -6, :] + 61.0/12.0*data[component_idx, -5, :] \
                                    - 13.0*data[component_idx, -4, :] + 107.0/6.0*data[component_idx, -3, :] \
                                    - 77.0/6.0*data[component_idx, -2, :] + 15.0/4.0*data[component_idx, -1, :])/(dx*dx)
            
            elif diff_data.ndim == 3:
                diff_data[0, :, :] = (15.0/4.0*data[component_idx, 0, :, :] - 77.0/6.0*data[component_idx, 1, :, :] \
                                      + 107.0/6.0*data[component_idx, 2, :, :] - 13.0*data[component_idx, 3, :, :] \
                                      + 61.0/12.0*data[component_idx, 4, :, :] - 5.0/6.0*data[component_idx, 5, :, :])/(dx*dx)
                
                diff_data[1, :, :] = (5.0/6.0*data[component_idx, 0, :, :] - 5.0/4.0*data[component_idx, 1, :, :] \
                                      - 1.0/3.0*data[component_idx, 2, :, :] + 7.0/6.0*data[component_idx, 3, :, :] \
                                      - 1.0/2.0*data[component_idx, 4, :, :] + 1.0/12.0*data[component_idx, 5, :, :])/(dx*dx)
                
                diff_data[-2, :, :] = (1.0/12.0*data[component_idx, -6, :, :] - 1.0/2.0*data[component_idx, -5, :, :] \
                                       + 7.0/6.0*data[component_idx, -4, :, :] - 1.0/3.0*data[component_idx, -3, :, :] \
                                       - 5.0/4.0*data[component_idx, -2, :, :] + 5.0/6.0*data[component_idx, -1, :, :])/(dx*dx)
                
                diff_data[-1, :, :] = (-5.0/6.0*data[component_idx, -6, :, :] + 61.0/12.0*data[component_idx, -5, :, :] \
                                       - 13.0*data[component_idx, -4, :, :] + 107.0/6.0*data[component_idx, -3, :, :] \
                                       - 77.0/6.0*data[component_idx, -2, :, :] + 15.0/4.0*data[component_idx, -1, :, :])/(dx*dx)
            
            else:
                raise RuntimeError('Data dimension > 3 not supported!')
        
        elif direction == 1:
            if diff_data.ndim < 2:
                raise RuntimeError('There is no second direction in data with less than two dimensions!')
            
            elif diff_data.ndim == 2:
                diff_data[:, 0] = (15.0/4.0*data[component_idx, :, 0] - 77.0/6.0*data[component_idx, :, 1] \
                                   + 107.0/6.0*data[component_idx, :, 2] - 13.0*data[component_idx, :, 3] \
                                   + 61.0/12.0*data[component_idx, :, 4] - 5.0/6.0*data[component_idx, :, 5])/(dx*dx)
                
                diff_data[:, 1] = (5.0/6.0*data[component_idx, :, 0] - 5.0/4.0*data[component_idx, :, 1] \
                                   - 1.0/3.0*data[component_idx, :, 2] + 7.0/6.0*data[component_idx, :, 3] \
                                   - 1.0/2.0*data[component_idx, :, 4] + 1.0/12.0*data[component_idx, :, 5])/(dx*dx)
                
                diff_data[:, -2] = (1.0/12.0*data[component_idx, :, -6] - 1.0/2.0*data[component_idx, :, -5] \
                                    + 7.0/6.0*data[component_idx, :, -4] - 1.0/3.0*data[component_idx, :, -3] \
                                    - 5.0/4.0*data[component_idx, :, -2] + 5.0/6.0*data[component_idx, :, -1])/(dx*dx)
                
                diff_data[:, -1] = (-5.0/6.0*data[component_idx, :, -6] + 61.0/12.0*data[component_idx, :, -5] \
                                    - 13.0*data[component_idx, :, -4] + 107.0/6.0*data[component_idx, :, -3] \
                                    - 77.0/6.0*data[component_idx, :, -2] + 15.0/4.0*data[component_idx, :, -1])/(dx*dx)
            
            elif diff_data.ndim == 3:
                diff_data[:, 0, :] = (15.0/4.0*data[component_idx, :, 0, :] - 77.0/6.0*data[component_idx, :, 1, :] \
                                      + 107.0/6.0*data[component_idx, :, 2, :] - 13.0*data[component_idx, :, 3, :] \
                                      + 61.0/12.0*data[component_idx, :, 4, :] - 5.0/6.0*data[component_idx, :, 5, :])/(dx*dx)
                
                diff_data[:, 1, :] = (5.0/6.0*data[component_idx, :, 0, :] - 5.0/4.0*data[component_idx, :, 1, :] \
                                      - 1.0/3.0*data[component_idx, :, 2, :] + 7.0/6.0*data[component_idx, :, 3, :] \
                                      - 1.0/2.0*data[component_idx, :, 4, :] + 1.0/12.0*data[component_idx, :, 5, :])/(dx*dx)
                
                diff_data[:, -2, :] = (1.0/12.0*data[component_idx, :, -6, :] - 1.0/2.0*data[component_idx, :, -5, :] \
                                       + 7.0/6.0*data[component_idx, :, -4, :] - 1.0/3.0*data[component_idx, :, -3, :] \
                                       - 5.0/4.0*data[component_idx, :, -2, :] + 5.0/6.0*data[component_idx, :, -1, :])/(dx*dx)
                
                diff_data[:, -1, :] = (-5.0/6.0*data[component_idx, :, -6, :] + 61.0/12.0*data[component_idx, :, -5, :] \
                                       - 13.0*data[component_idx, :, -4, :] + 107.0/6.0*data[component_idx, :, -3, :] \
                                       - 77.0/6.0*data[component_idx, :, -2, :] + 15.0/4.0*data[component_idx, :, -1, :])/(dx*dx)
            
            else:
                raise RuntimeError('Data dimension > 3 not supported!')
        
        elif direction == 2:
            if diff_data.ndim < 3:
                raise IOError('There is no third direction in data with less than three dimensions!')
            
            elif diff_data.ndim == 3:
                diff_data[:, :, 0] = (15.0/4.0*data[component_idx, :, :, 0] - 77.0/6.0*data[component_idx, :, :, 1] \
                                      + 107.0/6.0*data[component_idx, :, :, 2] - 13.0*data[component_idx, :, :, 3] \
                                      + 61.0/12.0*data[component_idx, :, :, 4] - 5.0/6.0*data[component_idx, :, :, 5])/(dx*dx)
                
                diff_data[:, :, 1] = (5.0/6.0*data[component_idx, :, :, 0] - 5.0/4.0*data[component_idx, :, :, 1] \
                                      - 1.0/3.0*data[component_idx, :, :, 2] + 7.0/6.0*data[component_idx, :, :, 3] \
                                      - 1.0/2.0*data[component_idx, :, :, 4] + 1.0/12.0*data[component_idx, :, :, 5])/(dx*dx)
                
                diff_data[:, :, -2] = (1.0/12.0*data[component_idx, :, :, -6] - 1.0/2.0*data[component_idx, :, :, -5] \
                                       + 7.0/6.0*data[component_idx, :, :, -4] - 1.0/3.0*data[component_idx, :, :, -3] \
                                       - 5.0/4.0*data[component_idx, :, :, -2] + 5.0/6.0*data[component_idx, :, :, -1])/(dx*dx)
                
                diff_data[:, :, -1] = (-5.0/6.0*data[component_idx, :, :, -6] + 61.0/12.0*data[component_idx, :, :, -5] \
                                       - 13.0*data[component_idx, :, :, -4] + 107.0/6.0*data[component_idx, :, :, -3] \
                                       - 77.0/6.0*data[component_idx, :, :, -2] + 15.0/4.0*data[component_idx, :, :, -1])/(dx*dx)
            
            else:
                raise RuntimeError('Data dimension > 3 not supported!')
    
    return diff_data


def computeSixthOrderSecondDerivative(data, dx, direction = 0, component_idx = 0, uses_one_sided = True):
    """
    Computing second derivative using explicit sixth order finite differencing.
    """

    data_shape = data.shape
    
    # Check whether the direction is valid.
    
    if direction < 0 or direction > 2:
        raise RuntimeError('Direction < 0 or > 2 is invalid!')
    
    # Check whether the dimension of data is valid.
    
    if data.ndim < 2:
        raise RuntimeError('Shape of data is invalid!')
    
    # Check whether the component_idx is valid.
    
    if component_idx >= data_shape[0] or component_idx < 0:
        raise RuntimeError('Component index is invalid!')
    
    # Check whether data size is large enough for sixth order second derivative.
    
    if uses_one_sided == True:
        if direction == 0:
            if data_shape[1] < 8:
                raise RuntimeError('First dimension of data is not large enough!')
        
        elif direction == 1:
            if data_shape[2] < 8:
                raise RuntimeError('Second dimension of data is not large enough!')
        
        elif direction == 2:
            if data_shape[3] < 8:
                raise RuntimeError('Third dimension of data is not large enough!')
    
    else:
        if direction == 0:
            if data_shape[1] < 7:
                raise RuntimeError('First dimension of data is not large enough!')
        
        elif direction == 1:
            if data_shape[2] < 7:
                raise RuntimeError('Second dimension of data is not large enough!')
        
        elif direction == 2:
            if data_shape[3] < 7:
                raise RuntimeError('Third dimension of data is not large enough!')
    
    # Initialize container to store the derivatives. The elements in the container
    # are initialized as NAN values.
    data_shape = numpy.delete(data_shape, [0])
    diff_data = numpy.empty(data_shape)
    diff_data[:] = numpy.NAN
    
    # Compute the derivatives in the interior of the domain.
    
    if direction == 0:
        if diff_data.ndim == 1:
            diff_data[3:-3] = (1.0/90.0*data[component_idx, 0:-6] - 3.0/20.0*data[component_idx, 1:-5] \
                               + 3.0/2.0*data[component_idx, 2:-4] - 49.0/18.0*data[component_idx, 3:-3] \
                               + 3.0/2.0*data[component_idx, 4:-2] - 3.0/20.0*data[component_idx, 5:-1] \
                               + 1.0/90.0*data[component_idx, 6:])/(dx*dx)
        
        elif diff_data.ndim == 2:
            diff_data[3:-3, :] = (1.0/90.0*data[component_idx, 0:-6, :] - 3.0/20.0*data[component_idx, 1:-5, :] \
                                  + 3.0/2.0*data[component_idx, 2:-4, :] - 49.0/18.0*data[component_idx, 3:-3, :] \
                                  + 3.0/2.0*data[component_idx, 4:-2, :] - 3.0/20.0*data[component_idx, 5:-1, :] \
                                  + 1.0/90.0*data[component_idx, 6:, :])/(dx*dx)
        
        elif diff_data.ndim == 3:
            diff_data[3:-3, :, :] = (1.0/90.0*data[component_idx, 0:-6, :, :] - 3.0/20.0*data[component_idx, 1:-5, :, :] \
                                     + 3.0/2.0*data[component_idx, 2:-4, :, :] - 49.0/18.0*data[component_idx, 3:-3, :, :] \
                                     + 3.0/2.0*data[component_idx, 4:-2, :, :] - 3.0/20.0*data[component_idx, 5:-1, :, :] \
                                     + 1.0/90.0*data[component_idx, 6:, :, :])/(dx*dx)
        
        else:
            raise RuntimeError('Data dimension > 3 not supported!')
    
    elif direction == 1:
        if diff_data.ndim < 2:
            raise IOError('There is no second direction in data with less than two dimensions!')
        
        elif diff_data.ndim == 2:
            diff_data[:, 3:-3] = (1.0/90.0*data[component_idx, :, 0:-6] - 3.0/20.0*data[component_idx, :, 1:-5] \
                                  + 3.0/2.0*data[component_idx, :, 2:-4] - 49.0/18.0*data[component_idx, :, 3:-3] \
                                  + 3.0/2.0*data[component_idx, :, 4:-2] - 3.0/20.0*data[component_idx, :, 5:-1] \
                                  + 1.0/90.0*data[component_idx, :, 6:])/(dx*dx)
        
        elif diff_data.ndim == 3:
            diff_data[:, 3:-3, :] = (1.0/90.0*data[component_idx, :, 0:-6, :] - 3.0/20.0*data[component_idx, :, 1:-5, :] \
                                     + 3.0/2.0*data[component_idx, :, 2:-4, :] - 49.0/18.0*data[component_idx, :, 3:-3, :] \
                                     + 3.0/2.0*data[component_idx, :, 4:-2, :] - 3.0/20.0*data[component_idx, :, 5:-1, :] \
                                     + 1.0/90.0*data[component_idx, :, 6:, :])/(dx*dx)
        
        else:
            raise RuntimeError('Data dimension > 3 not supported!')
    
    elif direction == 2:
        if diff_data.ndim < 3:
            raise IOError('There is no third direction in data with less than three dimensions!')
        
        elif diff_data.ndim == 3:
            diff_data[:, :, 3:-3] = (1.0/90.0*data[component_idx, :, :, 0:-6] - 3.0/20.0*data[component_idx, :, :, 1:-5] \
                                  + 3.0/2.0*data[component_idx, :, :, 2:-4] - 49.0/18.0*data[component_idx, :, :, 3:-3] \
                                  + 3.0/2.0*data[component_idx, :, :, 4:-2] - 3.0/20.0*data[component_idx, :, :, 5:-1] \
                                  + 1.0/90.0*data[component_idx, :, :, 6:])/(dx*dx)
        
        else:
            raise RuntimeError('Data dimension > 3 not supported!')
    
    # Compute the derivatives at the boundaries.
    
    if uses_one_sided == True:
        if direction == 0:
            if diff_data.ndim == 1:
                diff_data[0] = (469.0/90.0*data[component_idx, 0] - 223.0/10.0*data[component_idx, 1] \
                                + 879.0/20.0*data[component_idx, 2] - 949.0/18.0*data[component_idx, 3] \
                                + 41.0*data[component_idx, 4] - 201.0/10.0*data[component_idx, 5] \
                                + 1019.0/180.0*data[component_idx, 6] - 7.0/10.0*data[component_idx, 7])/(dx*dx)
                
                diff_data[1] = (7.0/10.0*data[component_idx, 0] - 7.0/18.0*data[component_idx, 1] \
                                - 27.0/10.0*data[component_idx, 2] + 19.0/4.0*data[component_idx, 3] \
                                - 67.0/18.0*data[component_idx, 4] + 9.0/5.0*data[component_idx, 5] \
                                - 1.0/2.0*data[component_idx, 6] + 11.0/180.0*data[component_idx, 7])/(dx*dx)
                
                diff_data[2] = (-11.0/180.0*data[component_idx, 0] + 107.0/90.0*data[component_idx, 1] \
                                - 21.0/10.0*data[component_idx, 2] + 13.0/18.0*data[component_idx, 3] \
                                + 17.0/36.0*data[component_idx, 4] - 3.0/10.0*data[component_idx, 5] \
                                + 4.0/45.0*data[component_idx, 6] - 1.0/90.0*data[component_idx, 7])/(dx*dx)
                
                diff_data[-3] = (-1.0/90.0*data[component_idx, -8] + 4.0/45.0*data[component_idx, -7] \
                                 - 3.0/10.0*data[component_idx, -6] + 17.0/36.0*data[component_idx, -5] \
                                 + 13.0/18.0*data[component_idx, -4] - 21.0/10.0*data[component_idx, -3] \
                                 + 107.0/90.0*data[component_idx, -2] - 11.0/180.0*data[component_idx, -1])/(dx*dx)
                
                diff_data[-2] = (11.0/180.0*data[component_idx, -8] - 1.0/2.0*data[component_idx, -7] \
                                 + 9.0/5.0*data[component_idx, -6] - 67.0/18.0*data[component_idx, -5] \
                                 + 19.0/4.0*data[component_idx, -4] - 27.0/10.0*data[component_idx, -3] \
                                 - 7.0/18.0*data[component_idx, -2] + 7.0/10.0*data[component_idx, -1])/(dx*dx)
                
                diff_data[-1] = (-7.0/10.0*data[component_idx, -8] + 1019.0/180.0*data[component_idx, -7] \
                                 - 201.0/10.0*data[component_idx, -6] + 41.0*data[component_idx, -5] \
                                 - 949.0/18.0*data[component_idx, -4] + 879.0/20.0*data[component_idx, -3] \
                                 - 223.0/10.0*data[component_idx, -2] + 469.0/90.0*data[component_idx, -1])/(dx*dx)
            
            elif diff_data.ndim == 2:
                diff_data[0, :] = (469.0/90.0*data[component_idx, 0, :] - 223.0/10.0*data[component_idx, 1, :] \
                                   + 879.0/20.0*data[component_idx, 2, :] - 949.0/18.0*data[component_idx, 3, :] \
                                   + 41.0*data[component_idx, 4, :] - 201.0/10.0*data[component_idx, 5, :] \
                                   + 1019.0/180.0*data[component_idx, 6, :] - 7.0/10.0*data[component_idx, 7, :])/(dx*dx)
                
                diff_data[1, :] = (7.0/10.0*data[component_idx, 0, :] - 7.0/18.0*data[component_idx, 1, :] \
                                   - 27.0/10.0*data[component_idx, 2, :] + 19.0/4.0*data[component_idx, 3, :] \
                                   - 67.0/18.0*data[component_idx, 4, :] + 9.0/5.0*data[component_idx, 5, :] \
                                   - 1.0/2.0*data[component_idx, 6, :] + 11.0/180.0*data[component_idx, 7, :])/(dx*dx)
                
                diff_data[2, :] = (-11.0/180.0*data[component_idx, 0, :] + 107.0/90.0*data[component_idx, 1, :] \
                                   - 21.0/10.0*data[component_idx, 2, :] + 13.0/18.0*data[component_idx, 3, :] \
                                   + 17.0/36.0*data[component_idx, 4, :] - 3.0/10.0*data[component_idx, 5, :] \
                                   + 4.0/45.0*data[component_idx, 6, :] - 1.0/90.0*data[component_idx, 7, :])/(dx*dx)
                
                diff_data[-3, :] = (-1.0/90.0*data[component_idx, -8, :] + 4.0/45.0*data[component_idx, -7, :] \
                                    - 3.0/10.0*data[component_idx, -6, :] + 17.0/36.0*data[component_idx, -5, :] \
                                    + 13.0/18.0*data[component_idx, -4, :] - 21.0/10.0*data[component_idx, -3, :] \
                                    + 107.0/90.0*data[component_idx, -2, :] - 11.0/180.0*data[component_idx, -1, :])/(dx*dx)
                
                diff_data[-2, :] = (11.0/180.0*data[component_idx, -8, :] - 1.0/2.0*data[component_idx, -7, :] \
                                    + 9.0/5.0*data[component_idx, -6, :] - 67.0/18.0*data[component_idx, -5, :] \
                                    + 19.0/4.0*data[component_idx, -4, :] - 27.0/10.0*data[component_idx, -3, :] \
                                    - 7.0/18.0*data[component_idx, -2, :] + 7.0/10.0*data[component_idx, -1, :])/(dx*dx)
                
                diff_data[-1, :] = (-7.0/10.0*data[component_idx, -8, :] + 1019.0/180.0*data[component_idx, -7, :] \
                                    - 201.0/10.0*data[component_idx, -6, :] + 41.0*data[component_idx, -5, :] \
                                    - 949.0/18.0*data[component_idx, -4, :] + 879.0/20.0*data[component_idx, -3, :] \
                                    - 223.0/10.0*data[component_idx, -2, :] + 469.0/90.0*data[component_idx, -1, :])/(dx*dx)
            
            elif diff_data.ndim == 3:
                diff_data[0, :, :] = (469.0/90.0*data[component_idx, 0, :, :] - 223.0/10.0*data[component_idx, 1, :, :] \
                                      + 879.0/20.0*data[component_idx, 2, :, :] - 949.0/18.0*data[component_idx, 3, :, :] \
                                      + 41.0*data[component_idx, 4, :, :] - 201.0/10.0*data[component_idx, 5, :, :] \
                                      + 1019.0/180.0*data[component_idx, 6, :, :] - 7.0/10.0*data[component_idx, 7, :, :])/(dx*dx)
                
                diff_data[1, :, :] = (7.0/10.0*data[component_idx, 0, :, :] - 7.0/18.0*data[component_idx, 1, :, :] \
                                      - 27.0/10.0*data[component_idx, 2, :, :] + 19.0/4.0*data[component_idx, 3, :, :] \
                                      - 67.0/18.0*data[component_idx, 4, :, :] + 9.0/5.0*data[component_idx, 5, :, :] \
                                      - 1.0/2.0*data[component_idx, 6, :, :] + 11.0/180.0*data[component_idx, 7, :, :])/(dx*dx)
                
                diff_data[2, :, :] = (-11.0/180.0*data[component_idx, 0, :, :] + 107.0/90.0*data[component_idx, 1, :, :] \
                                      - 21.0/10.0*data[component_idx, 2, :, :] + 13.0/18.0*data[component_idx, 3, :, :] \
                                      + 17.0/36.0*data[component_idx, 4, :, :] - 3.0/10.0*data[component_idx, 5, :, :] \
                                      + 4.0/45.0*data[component_idx, 6, :, :] - 1.0/90.0*data[component_idx, 7, :, :])/(dx*dx)
                
                diff_data[-3, :, :] = (-1.0/90.0*data[component_idx, -8, :, :] + 4.0/45.0*data[component_idx, -7, :, :] \
                                       - 3.0/10.0*data[component_idx, -6, :, :] + 17.0/36.0*data[component_idx, -5, :, :] \
                                       + 13.0/18.0*data[component_idx, -4, :, :] - 21.0/10.0*data[component_idx, -3, :, :] \
                                       + 107.0/90.0*data[component_idx, -2, :, :] - 11.0/180.0*data[component_idx, -1, :, :])/(dx*dx)
                
                diff_data[-2, :, :] = (11.0/180.0*data[component_idx, -8, :, :] - 1.0/2.0*data[component_idx, -7, :, :] \
                                       + 9.0/5.0*data[component_idx, -6, :, :] - 67.0/18.0*data[component_idx, -5, :, :] \
                                       + 19.0/4.0*data[component_idx, -4, :, :] - 27.0/10.0*data[component_idx, -3, :, :] \
                                       - 7.0/18.0*data[component_idx, -2, :, :] + 7.0/10.0*data[component_idx, -1, :, :])/(dx*dx)
                
                diff_data[-1, :, :] = (-7.0/10.0*data[component_idx, -8, :, :] + 1019.0/180.0*data[component_idx, -7, :, :] \
                                       - 201.0/10.0*data[component_idx, -6, :, :] + 41.0*data[component_idx, -5, :, :] \
                                       - 949.0/18.0*data[component_idx, -4, :, :] + 879.0/20.0*data[component_idx, -3, :, :] \
                                       - 223.0/10.0*data[component_idx, -2, :, :] + 469.0/90.0*data[component_idx, -1, :, :])/(dx*dx)
            
            else:
                raise RuntimeError('Data dimension > 3 not supported!')
        
        elif direction == 1:
            if diff_data.ndim < 2:
                raise RuntimeError('There is no second direction in data with less than two dimensions!')
            
            elif diff_data.ndim == 2:
                diff_data[:, 0] = (469.0/90.0*data[component_idx, :, 0] - 223.0/10.0*data[component_idx, :, 1] \
                                   + 879.0/20.0*data[component_idx, :, 2] - 949.0/18.0*data[component_idx, :, 3] \
                                   + 41.0*data[component_idx, :, 4] - 201.0/10.0*data[component_idx, :, 5] \
                                   + 1019.0/180.0*data[component_idx, :, 6] - 7.0/10.0*data[component_idx, :, 7])/(dx*dx)
                
                diff_data[:, 1] = (7.0/10.0*data[component_idx, :, 0] - 7.0/18.0*data[component_idx, :, 1] \
                                   - 27.0/10.0*data[component_idx, :, 2] + 19.0/4.0*data[component_idx, :, 3] \
                                   - 67.0/18.0*data[component_idx, :, 4] + 9.0/5.0*data[component_idx, :, 5] \
                                   - 1.0/2.0*data[component_idx, :, 6] + 11.0/180.0*data[component_idx, :, 7])/(dx*dx)
                
                diff_data[:, 2] = (-11.0/180.0*data[component_idx, :, 0] + 107.0/90.0*data[component_idx, :, 1] \
                                   - 21.0/10.0*data[component_idx, :, 2] + 13.0/18.0*data[component_idx, :, 3] \
                                   + 17.0/36.0*data[component_idx, :, 4] - 3.0/10.0*data[component_idx, :, 5] \
                                   + 4.0/45.0*data[component_idx, :, 6] - 1.0/90.0*data[component_idx, :, 7])/(dx*dx)
                
                diff_data[:, -3] = (-1.0/90.0*data[component_idx, :, -8] + 4.0/45.0*data[component_idx, :, -7] \
                                    - 3.0/10.0*data[component_idx, :, -6] + 17.0/36.0*data[component_idx, :, -5] \
                                    + 13.0/18.0*data[component_idx, :, -4] - 21.0/10.0*data[component_idx, :, -3] \
                                    + 107.0/90.0*data[component_idx, :, -2] - 11.0/180.0*data[component_idx, :, -1])/(dx*dx)
                
                diff_data[:, -2] = (11.0/180.0*data[component_idx, :, -8] - 1.0/2.0*data[component_idx, :, -7] \
                                    + 9.0/5.0*data[component_idx, :, -6] - 67.0/18.0*data[component_idx, :, -5] \
                                    + 19.0/4.0*data[component_idx, :, -4] - 27.0/10.0*data[component_idx, :, -3] \
                                    - 7.0/18.0*data[component_idx, :, -2] + 7.0/10.0*data[component_idx, :, -1])/(dx*dx)
                
                diff_data[:, -1] = (-7.0/10.0*data[component_idx, :, -8] + 1019.0/180.0*data[component_idx, :, -7] \
                                    - 201.0/10.0*data[component_idx, :, -6] + 41.0*data[component_idx, :, -5] \
                                    - 949.0/18.0*data[component_idx, :, -4] + 879.0/20.0*data[component_idx, :, -3] \
                                    - 223.0/10.0*data[component_idx, :, -2] + 469.0/90.0*data[component_idx, :, -1])/(dx*dx)
            
            elif diff_data.ndim == 3:
                diff_data[:, 0, :] = (469.0/90.0*data[component_idx, :, 0, :] - 223.0/10.0*data[component_idx, :, 1, :] \
                                      + 879.0/20.0*data[component_idx, :, 2, :] - 949.0/18.0*data[component_idx, :, 3, :] \
                                      + 41.0*data[component_idx, :, 4, :] - 201.0/10.0*data[component_idx, :, 5, :] \
                                      + 1019.0/180.0*data[component_idx, :, 6, :] - 7.0/10.0*data[component_idx, :, 7, :])/(dx*dx)
                
                diff_data[:, 1, :] = (7.0/10.0*data[component_idx, :, 0, :] - 7.0/18.0*data[component_idx, :, 1, :] \
                                      - 27.0/10.0*data[component_idx, :, 2, :] + 19.0/4.0*data[component_idx, :, 3, :] \
                                      - 67.0/18.0*data[component_idx, :, 4, :] + 9.0/5.0*data[component_idx, :, 5, :] \
                                      - 1.0/2.0*data[component_idx, :, 6, :] + 11.0/180.0*data[component_idx, :, 7, :])/(dx*dx)
                
                diff_data[:, 2, :] = (-11.0/180.0*data[component_idx, :, 0, :] + 107.0/90.0*data[component_idx, :, 1, :] \
                                      - 21.0/10.0*data[component_idx, :, 2, :] + 13.0/18.0*data[component_idx, :, 3, :] \
                                      + 17.0/36.0*data[component_idx, :, 4, :] - 3.0/10.0*data[component_idx, :, 5, :] \
                                      + 4.0/45.0*data[component_idx, :, 6, :] - 1.0/90.0*data[component_idx, :, 7, :])/(dx*dx)
                
                diff_data[:, -3, :] = (-1.0/90.0*data[component_idx, :, -8, :] + 4.0/45.0*data[component_idx, :, -7, :] \
                                       - 3.0/10.0*data[component_idx, :, -6, :] + 17.0/36.0*data[component_idx, :, -5, :] \
                                       + 13.0/18.0*data[component_idx, :, -4, :] - 21.0/10.0*data[component_idx, :, -3, :] \
                                       + 107.0/90.0*data[component_idx, :, -2, :] - 11.0/180.0*data[component_idx, :, -1, :])/(dx*dx)
                
                diff_data[:, -2, :] = (11.0/180.0*data[component_idx, :, -8, :] - 1.0/2.0*data[component_idx, :, -7, :] \
                                       + 9.0/5.0*data[component_idx, :, -6, :] - 67.0/18.0*data[component_idx, :, -5, :] \
                                       + 19.0/4.0*data[component_idx, :, -4, :] - 27.0/10.0*data[component_idx, :, -3, :] \
                                       - 7.0/18.0*data[component_idx, :, -2, :] + 7.0/10.0*data[component_idx, :, -1, :])/(dx*dx)
                
                diff_data[:, -1, :] = (-7.0/10.0*data[component_idx, :, -8, :] + 1019.0/180.0*data[component_idx, :, -7, :] \
                                       - 201.0/10.0*data[component_idx, :, -6, :] + 41.0*data[component_idx, :, -5, :] \
                                       - 949.0/18.0*data[component_idx, :, -4, :] + 879.0/20.0*data[component_idx, :, -3, :] \
                                       - 223.0/10.0*data[component_idx, :, -2, :] + 469.0/90.0*data[component_idx, :, -1, :])/(dx*dx)
            
            else:
                raise RuntimeError('Data dimension > 3 not supported!')
        
        elif direction == 2:
            if diff_data.ndim < 3:
                raise IOError('There is no third direction in data with less than three dimensions!')
            
            elif diff_data.ndim == 3:
                diff_data[:, :, 0] = (469.0/90.0*data[component_idx, :, :, 0] - 223.0/10.0*data[component_idx, :, :, 1] \
                                      + 879.0/20.0*data[component_idx, :, :, 2] - 949.0/18.0*data[component_idx, :, :, 3] \
                                      + 41.0*data[component_idx, :, :, 4] - 201.0/10.0*data[component_idx, :, :, 5] \
                                      + 1019.0/180.0*data[component_idx, :, :, 6] - 7.0/10.0*data[component_idx, :, :, 7])/(dx*dx)
                
                diff_data[:, :, 1] = (7.0/10.0*data[component_idx, :, :, 0] - 7.0/18.0*data[component_idx, :, :, 1] \
                                      - 27.0/10.0*data[component_idx, :, :, 2] + 19.0/4.0*data[component_idx, :, :, 3] \
                                      - 67.0/18.0*data[component_idx, :, :, 4] + 9.0/5.0*data[component_idx, :, :, 5] \
                                      - 1.0/2.0*data[component_idx, :, :, 6] + 11.0/180.0*data[component_idx, :, :, 7])/(dx*dx)
                
                diff_data[:, :, 2] = (-11.0/180.0*data[component_idx, :, :, 0] + 107.0/90.0*data[component_idx, :, :, 1] \
                                      - 21.0/10.0*data[component_idx, :, :, 2] + 13.0/18.0*data[component_idx, :, :, 3] \
                                      + 17.0/36.0*data[component_idx, :, :, 4] - 3.0/10.0*data[component_idx, :, :, 5] \
                                      + 4.0/45.0*data[component_idx, :, :, 6] - 1.0/90.0*data[component_idx, :, :, 7])/(dx*dx)
                
                diff_data[:, :, -3] = (-1.0/90.0*data[component_idx, :, :, -8] + 4.0/45.0*data[component_idx, :, :, -7] \
                                       - 3.0/10.0*data[component_idx, :, :, -6] + 17.0/36.0*data[component_idx, :, :, -5] \
                                       + 13.0/18.0*data[component_idx, :, :, -4] - 21.0/10.0*data[component_idx, :, :, -3] \
                                       + 107.0/90.0*data[component_idx, :, :, -2] - 11.0/180.0*data[component_idx, :, :, -1])/(dx*dx)
                
                diff_data[:, :, -2] = (11.0/180.0*data[component_idx, :, :, -8] - 1.0/2.0*data[component_idx, :, :, -7] \
                                       + 9.0/5.0*data[component_idx, :, :, -6] - 67.0/18.0*data[component_idx, :, :, -5] \
                                       + 19.0/4.0*data[component_idx, :, :, -4] - 27.0/10.0*data[component_idx, :, :, -3] \
                                       - 7.0/18.0*data[component_idx, :, :, -2] + 7.0/10.0*data[component_idx, :, :, -1])/(dx*dx)
                
                diff_data[:, :, -1] = (-7.0/10.0*data[component_idx, :, :, -8] + 1019.0/180.0*data[component_idx, :, :, -7] \
                                       - 201.0/10.0*data[component_idx, :, :, -6] + 41.0*data[component_idx, :, :, -5] \
                                       - 949.0/18.0*data[component_idx, :, :, -4] + 879.0/20.0*data[component_idx, :, :, -3] \
                                       - 223.0/10.0*data[component_idx, :, :, -2] + 469.0/90.0*data[component_idx, :, :, -1])/(dx*dx)
            
            else:
                raise RuntimeError('Data dimension > 3 not supported!')
    
    return diff_data

