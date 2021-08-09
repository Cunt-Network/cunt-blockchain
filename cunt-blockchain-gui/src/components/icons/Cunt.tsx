import React from 'react';
import { SvgIcon, SvgIconProps } from '@material-ui/core';
import { ReactComponent as CuntIcon } from './images/cunt.svg';

export default function Keys(props: SvgIconProps) {
  return <SvgIcon component={CuntIcon} viewBox="0 0 150 58" {...props} />;
}
